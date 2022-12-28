from azureml.core import Workspace
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.exceptions import ComputeTargetException
import yaml

ws = Workspace.from_config("../../resources/configs/workspace-config.json")
config = yaml.safe_load(open("../../resources/configs/config.yaml"))
compute_name = config['compute']['aml_compute']

try:
    compute = ComputeTarget(ws, compute_name)
    print(f"Using the existing compute '{compute_name}'.")
except ComputeTargetException:
    print("Provisioning compute cluster...")
    aml_comfig = AmlCompute.provisioning_configuration("STANDARD_D2_V2", min_nodes=0, max_nodes=2)
    compute = ComputeTarget.create(ws, compute_name, aml_comfig)
    compute.wait_for_completion(show_output=True)  # if min_nodes > 0 returns only after there are min_nodes provisioned
