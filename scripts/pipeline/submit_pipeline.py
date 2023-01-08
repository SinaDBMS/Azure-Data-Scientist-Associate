from azureml.core import Workspace, Environment, Experiment, RunConfiguration
from azureml.data import OutputFileDatasetConfig
from azureml.core.compute import ComputeInstance
from azureml.exceptions import ComputeTargetException
from azureml.pipeline.core import Pipeline
from azureml.pipeline.steps import PythonScriptStep

import sys
import yaml

config = yaml.safe_load(open("../../resources/configs/config.yaml"))
compute_instance_name = config['compute']['compute_instance']

# Loading the workspace
ws = Workspace.from_config("../../resources/configs/workspace-config.json")

# Connecting to the compute instance
try:
    compute = ComputeInstance(ws, compute_instance_name)
except ComputeTargetException:
    print(f"Compute instance '{compute_instance_name}' does not exist. Create one by running the code in "
          f"script/compute/compute_instance.py")
    sys.exit(1)

# Getting reference to a dataset
dataset = ws.datasets["diabetes"]

# Creating an environment
env = Environment.get(ws, "AzureML-sklearn-1.0-ubuntu20.04-py38-cpu")

# Creating a RunConfiguration object for the pipeline
pipeline_run_config = RunConfiguration()

pipeline_run_config.environment = env

pipeline_run_config.target = compute

# Creating the shared output file between pipeline steps
step1_output = OutputFileDatasetConfig("Output_Data")
step2_output = OutputFileDatasetConfig("Output_Data")

# Creating the pipeline steps
step_1 = PythonScriptStep(name="Step 1", script_name="step_1.py",
                          source_directory="./pipeline-steps", runconfig=pipeline_run_config,
                          arguments=["--input-data", dataset.as_named_input("Input_Data"),
                                           "--output-data", step1_output])

step_2 = PythonScriptStep(name="Step 2", script_name="step_2.py", source_directory="./pipeline-steps",
                          runconfig=pipeline_run_config,
                          arguments=["--input-data", step1_output.as_input("Input_Data"),
                                         "--output-data", step2_output]
                          )

step_3_1 = PythonScriptStep(name="Step 3.1", script_name="step_3_1.py", source_directory="./pipeline-steps",
                            runconfig=pipeline_run_config,
                            arguments=["--input-data", step2_output.as_input("Input_Data")]
                            )

step_3_2 = PythonScriptStep(name="Step 3.2", script_name="step_3_2.py", source_directory="./pipeline-steps",
                            runconfig=pipeline_run_config,
                            arguments=["--input-data", step2_output.as_input("Input_Data")]
                            )

# Creating pipeline
pipeline = Pipeline(ws, [step_1, step_2, step_3_1, step_3_2])

# Creating an Experiment
experiment = Experiment(ws, "Diabetes-Experiment-Pipeline")
pipeline_run = experiment.submit(pipeline)

pipeline_run.wait_for_completion(show_output=True)
