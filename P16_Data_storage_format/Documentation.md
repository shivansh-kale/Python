# Data Storage Formats in Python

In data science and machine learning workflows, datasets and models must often be stored and retrieved efficiently.

Python supports several data storage formats, each optimized for different use cases.

Common formats include:

* CSV
* JSON
* Pickle
* Parquet
* Feather
* HDF5
* Joblib

---

# 1. CSV (Comma Separated Values)

CSV is one of the most common data formats.

Example:

```text
Name,Age,Salary
Alice,25,60000
Bob,30,70000
```

Saving CSV:

```python
df.to_csv("data.csv", index=False)
```

Loading CSV:

```python
pd.read_csv("data.csv")
```

Advantages:

* human readable
* widely supported

Disadvantages:

* slower for large datasets
* no type information

---

# 2. JSON

JSON (JavaScript Object Notation) is widely used in APIs.

Example:

```json
{
  "Name": "Alice",
  "Age": 25
}
```

Saving JSON:

```python
df.to_json("data.json")
```

Loading JSON:

```python
pd.read_json("data.json")
```

Advantages:

* flexible structure
* common in web APIs

Disadvantages:

* inefficient for large tabular datasets

---

# 3. Pickle

Pickle serializes Python objects into binary format.

Example:

```python
import pickle

pickle.dump(object, file)
```

Loading:

```python
pickle.load(file)
```

Advantages:

* supports complex Python objects
* fast serialization

Disadvantages:

* not secure for untrusted data
* Python-specific format

---

# 4. Parquet

Parquet is a **columnar storage format** optimized for big data processing.

Example:

```python
df.to_parquet("data.parquet")
```

Advantages:

* very fast
* efficient compression
* ideal for large datasets

Widely used in:

* data engineering
* Spark
* analytics pipelines

---

# 5. Feather

Feather is designed for fast storage of DataFrames.

Example:

```python
df.to_feather("data.feather")
```

Advantages:

* extremely fast
* efficient for DataFrame exchange

Often used when transferring data between Python and R.

---

# 6. HDF5

HDF5 is designed for large-scale scientific data storage.

Example:

```python
df.to_hdf("data.h5", key="dataset")
```

Advantages:

* supports large datasets
* hierarchical structure

Commonly used in scientific computing.

---

# 7. Joblib

Joblib is commonly used for saving machine learning models.

Example:

```python
import joblib

joblib.dump(model, "model.joblib")
```

Loading:

```python
joblib.load("model.joblib")
```

Advantages:

* optimized for large NumPy arrays
* faster than pickle for ML models

---

# Choosing the Right Format

| Format  | Best For                  |
| ------- | ------------------------- |
| CSV     | small tabular datasets    |
| JSON    | APIs and structured data  |
| Pickle  | Python objects            |
| Parquet | large analytical datasets |
| Feather | fast DataFrame exchange   |
| HDF5    | scientific datasets       |
| Joblib  | machine learning models   |

---

# Summary

Different storage formats are optimized for different tasks.

Understanding these formats helps build efficient **data pipelines and ML workflows**.

In modern data systems:

* **Parquet** is preferred for large datasets
* **Joblib** is common for ML models
* **JSON** is used for APIs
* **CSV** is widely used for simple datasets
