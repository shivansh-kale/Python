"""
DATA VISUALIZATION IN PYTHON
----------------------------

Visualization helps understand patterns in data.

Two major Python libraries for visualization:

1. Matplotlib
2. Seaborn

Visualization is used heavily during:
- Exploratory Data Analysis (EDA)
- Feature analysis
- Model evaluation
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# =========================================================
# SAMPLE DATA
# =========================================================

data = {
    "Age": [22, 25, 47, 52, 46, 56, 23, 30],
    "Salary": [40000, 50000, 120000, 140000, 130000, 150000, 42000, 60000],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "Finance", "HR", "IT"]
}

df = pd.DataFrame(data)


# =========================================================
# 1. MATPLOTLIB BASICS
# =========================================================

"""
Matplotlib is the foundational plotting library in Python.
"""

# Line plot
plt.plot(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# =========================================================
# 2. HISTOGRAM (DISTRIBUTION)
# =========================================================

"""
Histograms show the distribution of numerical data.
"""

plt.hist(df["Salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


# =========================================================
# 3. SCATTER PLOT
# =========================================================

"""
Scatter plots show relationships between two variables.
"""

plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# =========================================================
# 4. BAR CHART
# =========================================================

"""
Bar charts compare categorical values.
"""

department_counts = df["Department"].value_counts()

plt.bar(department_counts.index, department_counts.values)
plt.title("Department Count")
plt.show()


# =========================================================
# 5. SEABORN INTRODUCTION
# =========================================================

"""
Seaborn is built on top of Matplotlib and provides
more attractive statistical plots.
"""

sns.set_style("whitegrid")


# =========================================================
# 6. SEABORN HISTOGRAM
# =========================================================

sns.histplot(df["Salary"], kde=True)

plt.title("Salary Distribution (Seaborn)")
plt.show()


# =========================================================
# 7. BOXPLOT (OUTLIER DETECTION)
# =========================================================

"""
Boxplots help identify outliers in data.
"""

sns.boxplot(x=df["Salary"])

plt.title("Salary Boxplot")
plt.show()


# =========================================================
# 8. COUNT PLOT (CATEGORICAL DATA)
# =========================================================

sns.countplot(x="Department", data=df)

plt.title("Department Frequency")
plt.show()


# =========================================================
# 9. CORRELATION HEATMAP
# =========================================================

"""
Heatmaps show correlation between numerical features.
"""

correlation = df.corr(numeric_only=True)

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Feature Correlation Heatmap")
plt.show()


# =========================================================
# 10. PAIRPLOT (EDA SUPER TOOL)
# =========================================================

"""
Pairplot visualizes relationships between multiple variables.
"""

sns.pairplot(df)

plt.show()