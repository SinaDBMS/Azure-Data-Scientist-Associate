from azureml.core import Workspace, Datastore, Dataset

ws = Workspace.from_config("../../resources/configs/workspace-config.json")
default_datastore = Datastore.get_default(ws)
dataset_name = "diabetes"

dataset = Dataset.File.upload_directory(src_dir="../../resources/datasets/", target=(default_datastore, "datasets/"),
                                        overwrite=True)
tabular_dataset = dataset.Tabular.from_delimited_files(path=(default_datastore, "datasets"))
tabular_dataset = tabular_dataset.register(ws, name=dataset_name, create_new_version=False, tags={'format': 'csv'})
