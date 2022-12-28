from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AksCompute
from azureml.exceptions import ComputeTargetException
import yaml

# Loading the workspace

ws = Workspace.from_config("../../resources/configs/workspace-config.json")

# Creating the aks compute
config = yaml.safe_load(open("../../resources/configs/config.yaml"))
compute_name = config['compute']['aks_compute']

try:
    compute = ComputeTarget(ws, compute_name)
    print(f"Using the existing compute '{compute_name}'.")
except ComputeTargetException:
    print(f"Compute '{compute_name}' does not exist. Creating one...")
    aks_config = AksCompute.provisioning_configuration(agent_count=3, vm_size="Standard_A3")
    compute = ComputeTarget.create(ws, compute_name, aks_config)
    compute.wait_for_completion(True)
