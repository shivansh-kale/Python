# 📦 Data Storage Formats in Python

In Machine Learning, Data Science, and Data Engineering, data needs to be **stored**, **shared**, **loaded**, and **processed efficiently**.

Different storage formats are optimized for different purposes:

- Human-readable data
- Fast loading/saving
- Compression
- Large-scale analytics
- Model serialization
- Cross-language compatibility

Choosing the right format can significantly improve performance and storage efficiency.

---

# 1️⃣ CSV (Comma-Separated Values)

CSV is the simplest and most widely used tabular data format.

Each row represents a record, and commas separate the columns.

Example:

```text
Name,Age,Salary
Alice,25,60000
Bob,30,70000
Charlie,28,75000
```

## Saving

```python
df.to_csv("data.csv", index=False)
```

## Loading

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

## Advantages

- Human-readable
- Supported by almost every software
- Easy to edit using Excel
- Good for small datasets

## Disadvantages

- Large file size
- Slow for big datasets
- Stores no datatype information
- No compression by default

## Best Used For

- Sharing datasets
- Small projects
- Import/export with Excel

---

# 2️⃣ JSON (JavaScript Object Notation)

JSON stores data as **key-value pairs**.

It is the standard format for APIs and web applications.

Example:

```json
{
    "Name": "Alice",
    "Age": 25,
    "Salary": 60000
}
```

Nested JSON:

```json
{
    "Employee": {
        "Name": "Alice",
        "Department": "AI",
        "Skills": [
            "Python",
            "ML"
        ]
    }
}
```

## Saving

```python
df.to_json("data.json")
```

## Loading

```python
df = pd.read_json("data.json")
```

## Advantages

- Human-readable
- Supports nested structures
- Perfect for APIs
- Language-independent

## Disadvantages

- Larger than binary formats
- Slower for huge datasets
- Not ideal for large tables

## Best Used For

- REST APIs
- Configuration files
- Data exchange between applications

---

# 3️⃣ Pickle

Pickle serializes **almost any Python object** into binary format.

It preserves Python objects exactly as they are.

Example:

```python
import pickle

model = {"name": "Linear Regression"}

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

Loading:

```python
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
```

## Advantages

- Stores almost any Python object
- Very easy to use
- Fast serialization

## Disadvantages

- Python-only
- Not secure for untrusted files
- Not human-readable

⚠️ Never load Pickle files from unknown sources.

## Best Used For

- Python objects
- Intermediate experiment results
- Small ML projects

---

# 4️⃣ Parquet

Parquet is a **columnar storage format** developed for big data analytics.

Unlike CSV, data is stored **column-wise** rather than row-wise.

```
CSV

Row 1
Row 2
Row 3
...

Parquet

Column A
Column B
Column C
...
```

Columnar storage makes analytical queries much faster because only the required columns are read.

## Saving

```python
df.to_parquet("data.parquet")
```

## Loading

```python
df = pd.read_parquet("data.parquet")
```

## Advantages

- Very fast
- Excellent compression
- Preserves datatypes
- Uses much less disk space
- Ideal for large datasets

## Disadvantages

- Not human-readable
- Requires additional libraries
  - pyarrow
  - fastparquet

## Best Used For

- Data Lakes
- Spark
- Hadoop
- Data Engineering
- Analytics pipelines
- Machine Learning pipelines

---

# 5️⃣ Feather

Feather is another binary columnar format built using Apache Arrow.

It focuses on **extremely fast DataFrame storage and retrieval.**

## Saving

```python
df.to_feather("data.feather")
```

## Loading

```python
df = pd.read_feather("data.feather")
```

## Advantages

- Extremely fast
- Lightweight
- Preserves datatypes
- Excellent for Python ↔ R communication

## Disadvantages

- Less compression than Parquet
- Mainly designed for DataFrames

## Best Used For

- Temporary datasets
- Fast local storage
- Sharing DataFrames between Python and R

---

# 6️⃣ HDF5 (Hierarchical Data Format)

HDF5 is designed for storing very large scientific datasets.

Unlike CSV, it supports **hierarchical groups**, similar to folders.

Example structure:

```text
Dataset.h5

├── Images
├── Labels
├── Metadata
└── Features
```

## Saving

```python
df.to_hdf(
    "data.h5",
    key="dataset"
)
```

## Loading

```python
df = pd.read_hdf(
    "data.h5",
    key="dataset"
)
```

## Advantages

- Efficient for huge datasets
- Hierarchical organization
- Fast random access
- Supports compression

## Disadvantages

- Not human-readable
- Less commonly used in modern ML than Parquet

## Best Used For

- Scientific Computing
- Medical Imaging
- Astronomy
- Simulation Data

---

# 7️⃣ Joblib

Joblib is specifically optimized for storing Machine Learning models.

It performs better than Pickle when objects contain large NumPy arrays.

## Saving

```python
import joblib

joblib.dump(
    model,
    "model.joblib"
)
```

## Loading

```python
model = joblib.load(
    "model.joblib"
)
```

## Advantages

- Faster than Pickle
- Efficient memory usage
- Optimized for NumPy arrays
- Common in Scikit-Learn

## Disadvantages

- Python-only
- Binary format
- Not secure for untrusted files

## Best Used For

- Scikit-Learn models
- Pipelines
- Preprocessors
- Encoders
- Feature transformers

---

# 🆚 Pickle vs Joblib

| Feature | Pickle | Joblib |
|----------|---------|---------|
| Python Objects | ✅ | ✅ |
| Large NumPy Arrays | ❌ | ✅ |
| Speed | Good | Faster |
| Compression | Limited | Better |
| ML Models | Good | Preferred |

---

# 🆚 CSV vs Parquet

| Feature | CSV | Parquet |
|----------|-----|----------|
| Human Readable | ✅ | ❌ |
| Compression | ❌ | ✅ |
| File Size | Large | Small |
| Speed | Slow | Fast |
| Stores Datatypes | ❌ | ✅ |
| Analytics | Poor | Excellent |

---

# 🆚 Parquet vs Feather

| Feature | Parquet | Feather |
|----------|----------|----------|
| Compression | Excellent | Moderate |
| Analytics | Excellent | Good |
| Read/Write Speed | Fast | Extremely Fast |
| Best For | Long-term storage | Temporary DataFrames |

---

# Installation

```bash
pip install pandas
pip install pyarrow
pip install fastparquet
pip install tables
pip install joblib
```

---

# Choosing the Right Format

| Format | Best For | Human Readable | Compression | Typical Use |
|---------|----------|----------------|-------------|-------------|
| CSV | Small datasets | ✅ | ❌ | Excel, sharing data |
| JSON | APIs | ✅ | ❌ | Web applications |
| Pickle | Python objects | ❌ | Moderate | Serialization |
| Parquet | Big data | ❌ | Excellent | Analytics, Spark |
| Feather | Fast DataFrames | ❌ | Good | Python ↔ R |
| HDF5 | Scientific data | ❌ | Good | Research |
| Joblib | ML models | ❌ | Good | Scikit-Learn models |

---

# 💡 Which Format Should You Use?

| Situation | Recommended Format |
|-----------|-------------------|
| Share data with anyone | CSV |
| Store API responses | JSON |
| Save Python objects | Pickle |
| Save Scikit-Learn models | Joblib |
| Large analytics datasets | Parquet |
| Fast DataFrame loading | Feather |
| Scientific experiments | HDF5 |

---

# Quick Decision Flow

```text
Need to store data?

        │
        ▼
Is it tabular data?
        │
   ┌────┴────┐
   │         │
 Yes        No
   │         │
Small?   Python Object?
   │         │
CSV      Pickle
   │
Large Dataset?
   │
   ▼
Parquet
   │
Need fastest DataFrame exchange?
   │
Feather
```

---

# Summary

| Format | Primary Purpose |
|----------|----------------|
| CSV | Universal tabular data |
| JSON | APIs and nested data |
| Pickle | Python object serialization |
| Parquet | Large-scale analytics |
| Feather | Fast DataFrame storage |
| HDF5 | Scientific computing |
| Joblib | Machine Learning models |

---

# Key Takeaways

- **CSV** → Universal and human-readable.
- **JSON** → Standard for APIs and nested data.
- **Pickle** → Serialize almost any Python object.
- **Joblib** → Best choice for Scikit-Learn models.
- **Parquet** → Industry standard for big data and analytics.
- **Feather** → Extremely fast DataFrame exchange.
- **HDF5** → Ideal for scientific and research datasets.

> **Rule of Thumb**
>
> - 📊 Small data → CSV
> - 🌐 APIs → JSON
> - 🧠 ML Models → Joblib
> - 🐍 Python Objects → Pickle
> - 🚀 Large Datasets → Parquet
> - ⚡ Fast DataFrame Sharing → Feather
> - 🔬 Scientific Data → HDF5
