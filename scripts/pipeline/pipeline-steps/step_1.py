import pandas as pd
import argparse
import os
from azureml.core import Run

print("Step 1")

# Parsing the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input-data", dest="input_data", type=str)
parser.add_argument("--output-data", dest="output_data", type=str)
args = parser.parse_args()

# Getting a reference to the run context
run = Run.get_context()

# Reading the intput dataset from run context
dataset: pd.DataFrame = run.input_datasets['Input_Data'].to_pandas_dataframe()

print(dataset)

# Altering the dataset
dataset["PatientID"] = 0

# Saving the dataset to the output location
dataset.to_csv(os.path.join(args.output_data, "data.csv"), index=False, header=True)
