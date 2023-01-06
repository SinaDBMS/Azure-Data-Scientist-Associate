from azureml.core import Workspace, Environment, ScriptRunConfig, Experiment, ComputeTarget
import yaml
import sys

# Reading the name of compute cluster from local config
from azureml.exceptions import ComputeTargetException

config = yaml.safe_load(open("../../resources/configs/config.yaml"))
compute_name = config['compute']['compute_instance']

# Load workspace
ws = Workspace.from_config("../../resources/configs/workspace-config.json")

# Using an existing environment
env = Environment.get(ws, "AzureML-sklearn-1.0-ubuntu20.04-py38-cpu")

# Loading the dataset
diabetes_dataset = ws.datasets.get("diabetes")
if diabetes_dataset is None:
    print("The dataset diabetes does not exist. Run the code under scripts/data/dataset.py to register the dataset.")
    sys.exit(1)

# Loading compute cluster
try:
    compute = ComputeTarget(ws, compute_name)
except ComputeTargetException:
    print(f"Compute {compute_name} does not exist. Create one by running the script aml-compute.py under compute.")
    sys.exit(1)

# Prepare to submit the experiment
script_run_config = ScriptRunConfig(source_directory="./diabetes-experiment", script="diabetes_training.py",
                                    arguments=['--regularization', 0.01,  # Regularization rate parameter
                                               '--input-data', diabetes_dataset.as_named_input('training_data')],
                                    environment=env,
                                    # compute_target=compute  # Comment out this line if you want to run locally.
                                    )
experiment = Experiment(ws, "Diabetes-Experiment")
run = experiment.submit(config=script_run_config)
run.wait_for_completion(True)

# Registering the model
run.register_model(model_name="Diabetes", model_path="outputs/diabetes_model.pkl",
                   properties={"AUC": run.get_metrics()["AUC"], "Accuracy": run.get_metrics()["Accuracy"]})
