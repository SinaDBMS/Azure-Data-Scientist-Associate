import sys
import yaml

from azureml.core import Workspace, Environment, Model
from azureml.core.model import InferenceConfig
from azureml.core.compute import ComputeTarget, AksCompute
from azureml.core.webservice import AksWebservice

# Loading the workspace
from azureml.exceptions import ComputeTargetException

ws = Workspace.from_config("../../resources/configs/workspace-config.json")

# Loading the config file
config = yaml.safe_load(open("../../resources/configs/config.yaml"))

# Loading the model
model_name = "Diabetess"
try:
    model = ws.models[model_name]
except KeyError:
    print(f"Model '{model_name}' does not exist. Train and register one by running the code in "
          f"scripts/train/submit_experiment.")
    sys.exit(1)

# Using an existing environment
env = Environment("aks-service-env")
python_packages = ["joblib", "scikit-learn"]
for pip_package in python_packages:
    env.python.conda_dependencies.add_pip_package(pip_package)

# Creating inference config
inference_config = InferenceConfig(source_directory="diabetes-service", entry_script="diabetes_training.py",
                                   environment=env)

aks_deployment_config = AksWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Using an existing compute target
compute_name = config['compute']['aks_compute']
try:
    compute = ComputeTarget(ws, compute_name)
except ComputeTargetException:
    print(f"Compute '{compute_name}' does not exist. Create one by running the code in scripts/compute/aks_compute.py.")
    sys.exit(1)

aks_service = Model.deploy(ws, "diabetes-aks-service", [model], inference_config, aks_deployment_config, compute)
aks_service.wait_for_deployment(True)
