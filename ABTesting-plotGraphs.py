import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# # Step 1: Read the data file into a pandas DataFrame
# file_path1 = 'data/sample_data.csv'
# df = pd.read_csv(file_path1, sep=',', header=0)

# # Step 2: Perform data manipulation and analysis
# # Example: Calculate the mean of a column
# mean_value = df['total_clicks'].mean()
# print(f"Mean value of total_clicks: {mean_value}")

# # Example: Filter rows based on a condition
# filtered_df = df[df['total_clicks'] > 1]
# print("Filtered DataFrame:")
# print(filtered_df)
# # Print by formating the data with labels - Iterate over rows of the filtered_df
# # for index, row in filtered_df.iterrows():
# #     print(f"Index: {index}, Customer Id: {row['customer_id']}, Total Days: {row['total_days']}")

# # Step 3: Visualize the data using matplotlib
# # Example: Plot a bar chart
# filtered_df.plot(kind='bar', x='date', y='total_clicks', title='Bar Chart Example')

# # Show the plot
# plt.show()


# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array
# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show()

# sns.displot([0, 1, 2, 3, 4, 5], hist=False) #without histogram
# plt.show()

# sns.displot(arr, hist=False) #visualize the random distribution of the array

# probability distribution of many events, eg. IQ Scores, Heartbeat etc.
from numpy import random
x = random.normal(size=(2, 3)) #Generate a random normal distribution of size 2x3  
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3)) #Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2
print(x)

# sns.displot(x)
# Adding titles to the plots
sns.displot(x, kind="kde").set(title='Kernel Density Estimation')
plt.show()

sns.displot(x, kind="hist").set(title='Histogram')
plt.show()

sns.displot(x, kind="ecdf").set(title='Empirical Cumulative Distribution Function')
plt.show()

sns.displot(x, kind="kde", rug=True).set(title='Kernel Density Estimation with Rug Plot')
plt.show()

# sns.displot(x, kind="kde", rug=True, rug_kws={"color": "g"}, kde_kws={"color": "k", "lw": 3}, hist_kws={"histtype": "step", "linewidth": 3, "alpha": 1, "color": "g"}).set(title='Customized Kernel Density Estimation with Rug Plot')
# plt.show()

sns.kdeplot(x).set(title='Kernel Density Estimation')
plt.show()