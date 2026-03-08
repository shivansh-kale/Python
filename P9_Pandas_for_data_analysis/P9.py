"""
DATA ANALYSIS AND MANIPULATION WITH PANDAS
------------------------------------------

Pandas is a powerful Python library for data manipulation and analysis.

It provides two main data structures:
1. Series
2. DataFrame

Pandas is widely used for:
- cleaning datasets
- exploratory data analysis
- feature engineering
- preprocessing for machine learning
"""

import pandas as pd


# =========================================================
# 1. PANDAS SERIES
# =========================================================

"""
A Series is a one-dimensional labeled array.
It is similar to a column in a table.
"""

data = [10, 20, 30, 40]

series = pd.Series(data)

print(series)


# Series with custom index
series = pd.Series(data, index=["a", "b", "c", "d"])

print(series)


# =========================================================
# 2. DATAFRAMES
# =========================================================

"""
A DataFrame is a 2-dimensional labeled table.

Think of it like a spreadsheet or SQL table.
"""

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 22, 23],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

print(df)


# =========================================================
# 3. INDEXING AND FILTERING
# =========================================================

"""
Pandas provides powerful ways to access and filter data.
"""

# Select column
print(df["Name"])

# Select multiple columns
print(df[["Name", "Age"]])

# Select row using loc
print(df.loc[0])

# Select row using iloc
print(df.iloc[1])

# Filtering data
filtered = df[df["Age"] > 21]

print(filtered)


# =========================================================
# 4. GROUPBY AND AGGREGATION
# =========================================================

"""
GroupBy allows grouping rows and applying aggregation functions.
"""

data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Salary": [60000, 70000, 50000, 52000]
}

df = pd.DataFrame(data)

# Group by department
grouped = df.groupby("Department")

# Calculate mean salary
print(grouped["Salary"].mean())


# Multiple aggregations
print(grouped["Salary"].agg(["mean", "max", "min"]))


# =========================================================
# 5. HANDLING MISSING VALUES
# =========================================================

"""
Real-world datasets often contain missing values.
"""

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, None, 23]
}

df = pd.DataFrame(data)

print(df)

# Detect missing values
print(df.isnull())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

# Drop missing rows
df.dropna()


# =========================================================
# 6. MERGING AND JOINING
# =========================================================

"""
Combining datasets is very common in data analysis.
"""

students = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

scores = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Score": [85, 90, 95]
})

# Merge datasets
merged = pd.merge(students, scores, on="StudentID")

print(merged)


# =========================================================
# 7. TIME SERIES BASICS
# =========================================================

"""
Pandas provides strong support for time-series data.
"""

dates = pd.date_range(start="2024-01-01", periods=5)

data = {
    "Date": dates,
    "Sales": [100, 120, 150, 130, 170]
}

df = pd.DataFrame(data)

df.set_index("Date", inplace=True)

print(df)

# Resampling example (daily to monthly)
print(df.resample("M").sum())