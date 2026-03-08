"""
DATA STORAGE FORMATS IN PYTHON
------------------------------

This file demonstrates common data storage formats used in
data science and machine learning.

Topics covered:

1. CSV
2. JSON
3. Pickle
4. Parquet
5. Feather
6. HDF5
7. Joblib for ML models
"""

import pandas as pd
import json
import pickle
import joblib


# =========================================================
# SAMPLE DATASET
# =========================================================

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [60000, 70000, 80000]
}

df = pd.DataFrame(data)

print(df)


# =========================================================
# 1. CSV FORMAT
# =========================================================

"""
CSV (Comma Separated Values) is one of the most common
data storage formats.
"""

# Save to CSV
df.to_csv("data.csv", index=False)

# Load CSV
csv_df = pd.read_csv("data.csv")

print("CSV loaded:")
print(csv_df)


# =========================================================
# 2. JSON FORMAT
# =========================================================

"""
JSON is widely used in APIs and configuration files.
"""

# Save JSON
df.to_json("data.json", orient="records")

# Load JSON
json_df = pd.read_json("data.json")

print("JSON loaded:")
print(json_df)


# =========================================================
# 3. PICKLE FORMAT
# =========================================================

"""
Pickle serializes Python objects into binary format.
"""

with open("data.pkl", "wb") as f:
    pickle.dump(df, f)

with open("data.pkl", "rb") as f:
    pickle_df = pickle.load(f)

print("Pickle loaded:")
print(pickle_df)


# =========================================================
# 4. PARQUET FORMAT
# =========================================================

"""
Parquet is a columnar storage format optimized for big data.
"""

df.to_parquet("data.parquet")

parquet_df = pd.read_parquet("data.parquet")

print("Parquet loaded:")
print(parquet_df)


# =========================================================
# 5. FEATHER FORMAT
# =========================================================

"""
Feather is designed for fast data frame storage.
"""

df.to_feather("data.feather")

feather_df = pd.read_feather("data.feather")

print("Feather loaded:")
print(feather_df)


# =========================================================
# 6. HDF5 FORMAT
# =========================================================

"""
HDF5 is used for storing large datasets efficiently.
"""

df.to_hdf("data.h5", key="dataset", mode="w")

hdf_df = pd.read_hdf("data.h5", key="dataset")

print("HDF5 loaded:")
print(hdf_df)


# =========================================================
# 7. JOBLIB (MODEL STORAGE)
# =========================================================

"""
Joblib is commonly used to store machine learning models.
"""

joblib.dump(df, "data.joblib")

loaded_df = joblib.load("data.joblib")

print("Joblib loaded:")
print(loaded_df)