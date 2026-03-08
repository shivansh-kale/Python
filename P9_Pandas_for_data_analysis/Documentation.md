# Data Analysis & Manipulation with Pandas

Pandas is one of the most important libraries in the Python data ecosystem.

It provides powerful tools for:

* data cleaning
* data manipulation
* data exploration
* feature engineering

Pandas is built on top of **NumPy** and is widely used in:

* machine learning pipelines
* financial analysis
* data science
* research computing

---

# 1. Pandas Series

A **Series** is a one-dimensional labeled array.

Example:

```python
import pandas as pd

data = [10, 20, 30]

series = pd.Series(data)
```

A Series consists of:

* values
* index labels

Example with custom index:

```python
series = pd.Series(data, index=["a","b","c"])
```

---

# 2. DataFrames

A **DataFrame** is a two-dimensional table of data.

It is similar to:

* Excel spreadsheet
* SQL table
* dataset matrix

Example:

```python
data = {
    "Name": ["Alice", "Bob"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)
```

Structure of DataFrame:

| Index | Name  | Age |
| ----- | ----- | --- |
| 0     | Alice | 21  |
| 1     | Bob   | 22  |

---

# 3. Indexing and Filtering

Pandas provides multiple ways to access data.

## Column Selection

```python
df["Name"]
```

Multiple columns:

```python
df[["Name","Age"]]
```

---

## Row Selection

Using `loc` (label-based):

```python
df.loc[0]
```

Using `iloc` (position-based):

```python
df.iloc[1]
```

---

## Filtering

Example:

```python
df[df["Age"] > 21]
```

Filtering is commonly used during **data cleaning and preprocessing**.

---

# 4. GroupBy and Aggregation

The **GroupBy operation** allows splitting data into groups and applying aggregation functions.

Example dataset:

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Alice    | 60000  |
| IT         | Bob      | 70000  |
| HR         | Charlie  | 50000  |

Example:

```python
df.groupby("Department")["Salary"].mean()
```

Multiple aggregations:

```python
df.groupby("Department")["Salary"].agg(["mean","max","min"])
```

GroupBy is essential for **summarizing datasets**.

---

# 5. Handling Missing Values

Real-world datasets often contain missing values.

Example:

```python
df.isnull()
```

Handling missing values:

### Fill missing values

```python
df.fillna(0)
```

### Fill with mean

```python
df["Age"].fillna(df["Age"].mean())
```

### Drop missing rows

```python
df.dropna()
```

Handling missing data is a **critical step in machine learning preprocessing**.

---

# 6. Merging and Joining

Datasets often come from multiple sources and need to be combined.

Example tables:

Students table:

| StudentID | Name  |
| --------- | ----- |
| 1         | Alice |
| 2         | Bob   |

Scores table:

| StudentID | Score |
| --------- | ----- |
| 1         | 85    |
| 2         | 90    |

Merge operation:

```python
pd.merge(students, scores, on="StudentID")
```

Types of joins:

| Join Type | Description      |
| --------- | ---------------- |
| inner     | common rows      |
| left      | keep left table  |
| right     | keep right table |
| outer     | union of both    |

---

# 7. Time-Series Basics

Pandas provides powerful tools for working with time-based data.

Example date range:

```python
pd.date_range(start="2024-01-01", periods=5)
```

Example dataset:

```python
df.set_index("Date")
```

Time-series operations include:

* resampling
* rolling averages
* time shifting

Example resampling:

```python
df.resample("M").sum()
```

Time-series analysis is widely used in:

* financial data
* forecasting models
* sensor data analysis

---

# Summary

Pandas is the primary tool for data manipulation in Python.

| Concept        | Purpose                    |
| -------------- | -------------------------- |
| Series         | one-dimensional data       |
| DataFrame      | tabular dataset            |
| indexing       | selecting rows and columns |
| filtering      | conditional data selection |
| groupby        | grouping and aggregation   |
| missing values | data cleaning              |
| merge/join     | combining datasets         |
| time-series    | working with temporal data |

Mastering Pandas is essential before learning:

* machine learning pipelines
* feature engineering
* data visualization
* model training
