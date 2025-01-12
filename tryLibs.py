# pandas is a powerful and flexible open-source data analysis and data manipulation library for Python. 
# It provides data structures and functions needed to work with structured data seamlessly. 
# It is widely used for data cleaning, preparation, and analysis in data science, machine learning, and scientific computing.
import pandas as pd
# Key Features of pandas:
# DataFrame: A 2-dimensional labeled data structure with columns of potentially different types, similar to a table in a database or an Excel spreadsheet.
# Series: A 1-dimensional labeled array capable of holding any data type.
# Data Alignment: Automatic and explicit data alignment, making it easy to handle missing data.
# Reshaping and Pivoting: Tools for reshaping and pivoting datasets.
# Data Aggregation: Functions for aggregating and summarizing data.
# Time Series: Powerful tools for working with time series data.
# File I/O: Functions for reading and writing data between in-memory data structures and different file formats (e.g., CSV, Excel, SQL databases).

# Create a DataFrame
print("###################### Creating a DataFrame:")
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

ages = df['Age']
print("####################### Ages:\n", ages)

filtered_df = df[df['Age'] > 28]
print("####################### Filtered DataFrame, Age > 28:\n", filtered_df)

# Add a new column
df['Salary'] = [70000, 80000, 90000]
print("####################### DataFrame with Salary:\n", df)

# fundamental package for scientific computing in Python. 
# It provides support for large, multi-dimensional arrays and matrices, 
# along with a collection of mathematical functions to operate on these arrays efficiently.
import numpy as np

# comprehensive library for creating static, animated, and interactive visualizations in Python. 
# It is widely used for plotting and data visualization in scientific computing, data analysis, and machine learning.
import matplotlib.pyplot as plt


# Create a 1D array
a = np.array([1, 2, 3, 4, 5])

# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])

# Perform element-wise operations
c = a * 2
d = b + 3

# Calculate the mean of an array
mean_a = np.mean(a)

# Perform matrix multiplication
e = np.dot(b, b.T)

print("1D array:", a)
print("2D array:\n", b)
print("Element-wise multiplication:", c)
print("Element-wise addition:\n", d)
print("Mean of 1D array:", mean_a)
print("Matrix multiplication:\n", e)


np.random.seed(42)

x = np.random.binomial(n=1, p=0.6, size=15)
y = np.random.binomial(n=1, p=0.4, size=19)

_, (a, c) = np.unique(x, return_counts=True)
_, (b, d) = np.unique(y, return_counts=True)

df = pd.DataFrame(data=[[a, b], [c, d]], 
                 index=["click", "no click"], 
                 columns=["A", "B"])
m = df.values

print("- Observations:")
print(f"  - Version A: = {x}")
print(f"  - Version B: = {y}")
print("###################### Contingency table:")
print(df)


