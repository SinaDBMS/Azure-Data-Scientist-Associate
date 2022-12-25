from azureml.core import Workspace
from azureml.core.compute import ComputeInstance, ComputeTarget
from azureml.exceptions import ComputeTargetException

ws = Workspace.from_config("../../resources/configs/workspace-config.json")

compute_name = "single-instance-compute"

try:
    compute = ComputeTarget(ws, compute_name)
    print(f"Using the existing {compute_name}.")
except ComputeTargetException:
    print("Provisioning compute instance...")
    compute_instance_config = ComputeInstance.provisioning_configuration(vm_size="Standard_DS1_v2")
    compute = ComputeTarget.create(ws, compute_name, compute_instance_config)
    compute.wait_for_completion(show_output=True)
