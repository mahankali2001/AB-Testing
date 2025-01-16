import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read the data file into a pandas DataFrame
file_path1 = 'data/sample_data.csv'
df = pd.read_csv(file_path1, sep=',', header=0)

# Step 2: Perform data manipulation and analysis
# Example: Calculate the mean of a column
mean_value = df['total_clicks'].mean()
print(f"Mean value of total_clicks: {mean_value}")

# Example: Filter rows based on a condition
filtered_df = df[df['total_clicks'] > 1]
print("Filtered DataFrame:")
print(filtered_df)
# Print by formating the data with labels - Iterate over rows of the filtered_df
# for index, row in filtered_df.iterrows():
#     print(f"Index: {index}, Customer Id: {row['customer_id']}, Total Days: {row['total_days']}")