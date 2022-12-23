from azureml.core import Workspace
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.exceptions import ComputeTargetException

ws = Workspace.from_config("../../resources/configs/workspace-config.json")
compute_name = "AML-Compute"

try:
    compute = ComputeTarget(ws, compute_name)
except ComputeTargetException:
    print("Compute does not exist. Creating one...")
    aml_comfig = AmlCompute.provisioning_configuration("STANDARD_D2_V2", min_nodes=0, max_nodes=2)
    compute = ComputeTarget.create(ws, compute_name, aml_comfig)
    compute.wait_for_completion(show_output=True)  # if min_nodes > 0 returns only after there are min_nodes provisioned
