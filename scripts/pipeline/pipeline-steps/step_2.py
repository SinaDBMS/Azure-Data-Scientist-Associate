import pandas as pd
import argparse
import os

print("Step 2")

# Parsing the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input-data", type=str, dest="input_data")
parser.add_argument("--output-data", type=str, dest="output_data")
args = parser.parse_args()

# Reading the input data from the location provided
dataframe = pd.read_csv(os.path.join(args.input_data, "data.csv"))

print(dataframe)

# Altering the dataset
dataframe["Pregnancies"] = 1

# Saving the dataset to the shared output location
dataframe.to_csv(os.path.join(args.output_data, "data.csv"), index=False)
