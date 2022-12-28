from azureml.core import Workspace, Model, Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

# Load workspace
ws = Workspace.from_config("../../resources/configs/workspace-config.json")

# Load a model
model = ws.models['Diabetes']

# Create Environment for deployment
env = Environment("aci-service-env")
env.python.conda_dependencies.add_pip_package("joblib")
env.python.conda_dependencies.add_pip_package("scikit-learn")

# Creating inference config
inference_config = InferenceConfig(source_directory="./diabetes-service", entry_script="score_diabetes.py",
                                   environment=env)

# Creating deployment config for an aci webservice
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)
aci_service = Model.deploy(ws, "diabetes-aci-service", [model], inference_config, deployment_config, overwrite=True)
aci_service.wait_for_deployment(True)
