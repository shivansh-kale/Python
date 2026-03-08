# Data Visualization in Python

Data visualization is a crucial step in **Exploratory Data Analysis (EDA)**.

It helps analysts and machine learning engineers:

* understand data distributions
* detect outliers
* identify correlations
* visualize relationships between variables

Two primary libraries used in Python are:

* **Matplotlib**
* **Seaborn**

---

# 1. Matplotlib

Matplotlib is the foundational visualization library in Python.

It provides complete control over plots and is used by many other libraries.

Import example:

```python
import matplotlib.pyplot as plt
```

---

# 2. Line Plot

Line plots show trends or relationships between variables.

Example:

```python
plt.plot(x, y)
plt.title("Line Plot")
plt.show()
```

Common uses:

* time series analysis
* performance tracking
* trend visualization

---

# 3. Histogram

Histograms visualize the distribution of numerical data.

Example:

```python
plt.hist(data, bins=10)
```

Histograms help identify:

* skewness
* data distribution
* outliers

---

# 4. Scatter Plot

Scatter plots show relationships between two variables.

Example:

```python
plt.scatter(x, y)
```

They are often used to:

* detect correlations
* visualize clusters
* analyze feature relationships

---

# 5. Bar Chart

Bar charts compare categorical values.

Example:

```python
plt.bar(categories, values)
```

Example use cases:

* sales comparison
* category frequency
* survey results

---

# 6. Seaborn

Seaborn is built on top of Matplotlib and provides more visually appealing statistical plots.

Import example:

```python
import seaborn as sns
```

Advantages of Seaborn:

* better default styles
* simpler syntax
* built-in statistical plots

---

# 7. Histogram with KDE

Seaborn provides improved distribution plots.

Example:

```python
sns.histplot(data, kde=True)
```

KDE (Kernel Density Estimation) provides a smooth distribution curve.

---

# 8. Boxplot

Boxplots help identify:

* median
* quartiles
* outliers

Example:

```python
sns.boxplot(x=data)
```

Boxplots are commonly used in **data cleaning**.

---

# 9. Count Plot

Count plots visualize frequency of categorical variables.

Example:

```python
sns.countplot(x="category", data=df)
```

Useful for analyzing class imbalance in datasets.

---

# 10. Correlation Heatmap

Heatmaps visualize correlation between numerical features.

Example:

```python
sns.heatmap(df.corr(), annot=True)
```

Correlation values range from:

| Value | Meaning                     |
| ----- | --------------------------- |
| +1    | strong positive correlation |
| 0     | no correlation              |
| -1    | strong negative correlation |

---

# 11. Pairplot

Pairplot automatically creates pairwise plots between features.

Example:

```python
sns.pairplot(df)
```

Pairplots help quickly explore relationships in datasets.

---

# Summary

Data visualization is essential for understanding datasets before training models.

| Plot Type    | Purpose                  |
| ------------ | ------------------------ |
| Line plot    | trend analysis           |
| Histogram    | data distribution        |
| Scatter plot | feature relationships    |
| Bar chart    | category comparison      |
| Boxplot      | outlier detection        |
| Heatmap      | feature correlation      |
| Pairplot     | multivariate exploration |

Visualization plays a key role in **EDA, feature engineering, and model interpretation**.
