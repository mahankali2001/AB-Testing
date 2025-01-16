import numpy as np 
import scipy as stats
from scipy.stats import ttest_ind


# T-Test - determine if there is significant deference between means of two variables and lets us know if they belong to the same distribution.
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
alpha = 0.05
# print(res)
p_value = res.pvalue
print('pvalue: ' + str(p_value))
statistic = res.statistic
print('statistic: ' + str(statistic)) #t-statistic value is a measure of the difference between the two groups. A larger absolute value indicates a more significant difference
if p_value <= alpha:
    print("Reject the null hypothesis: There is a significant difference between the means.\n")
else:
    print("Fail to reject the null hypothesis: No significant difference between the means.\n")

# Scenario: Suppose you have test scores for two groups of students, 
# Group A and Group B, who were taught using different teaching methods. 
# You want to check if the difference in their mean scores is statistically significant.

# Data:
# Group A: [85, 88, 90, 92, 94]
# Group B: [78, 82, 85, 87, 89]
# Hypotheses:
# Null Hypothesis (H0): The means of Group A and Group B are equal (no significant difference).
# Alternative Hypothesis (H1): The means of Group A and Group B are not equal (significant difference exists).
# Significance Level (𝛼): 0.05 (5%)

# Data
print(f"Usecase: Compare the means of two groups of students.\n")


group_a = [85, 88, 90, 92, 94]
group_b = [78, 82, 85, 87, 89]

# Perform t-test
t_stat, p_value = ttest_ind(group_a, group_b)

# Results
print(f"T-Statistic: {t_stat:.2f}")
print(f"P-Value: {p_value:.4f}")

# Interpret the results
alpha = 0.05
if p_value <= alpha:
    print("Reject the null hypothesis: There is a significant difference between the means.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the means.")