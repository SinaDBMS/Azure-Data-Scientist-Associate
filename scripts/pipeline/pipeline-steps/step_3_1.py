import pandas as pd
import os
import argparse

print("Step 3.1")

# Parsing the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--input-data", type=str, dest="input_data")
args = parser.parse_args()

# Reading the input data from the location provided
dataframe = pd.read_csv(os.path.join(args.input_data, "data.csv"))

print(dataframe)
