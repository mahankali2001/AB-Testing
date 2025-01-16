import numpy as np
from scipy import stats

def mean(data):
    l = len(data)
    total  = 0
    for i in range(l):
        total += data[i]
    return total / l

data = [10, 20, 20, 30, 40]
print(mean(data))

def median(data):
    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    middle = round(n/2)-1
    print(middle)
    if n%2 == 0:
        return (data[middle] + data [middle+1]) / 2
    else:
        return data[middle]

data = [10, 20, 20, 30, 40]
print(median(data))

data = [10, 20, 20, 30, 40, 50]
print(median(data))


def descriptive_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    mode_result = stats.mode(data)
    # mode = mode_result.mode[0] if mode_result.count[0] > 0 else None
    std_dev = np.std(data)
    return {'mean': mean, 'median': median, 'std_dev': std_dev, 'mode': mode_result} #'mode': mode

data = [10, 20, 20, 30, 40]
print(descriptive_stats(data))

data = [10, 20, 20, 30, 40, 50]
print(descriptive_stats(data))

# Hypothesis Testing (t-test) - Given two independent samples, conduct a t-test to check if there is a significant difference between them.
def t_test(sample1, sample2):
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    return t_stat, p_value

sample1 = [10, 12, 13, 15, 18]
sample2 = [20, 22, 24, 26, 28]
t_stat, p_value = t_test(sample1, sample2)
print(f"T-statistic: {t_stat}, P-value: {p_value}")

# ANOVA (Analysis of Variance) - Given three samples, perform a one-way ANOVA to see if there's a significant difference between them.
def anova_test(*samples):
    f_stat, p_value = stats.f_oneway(*samples)
    return f_stat, p_value

group1 = [5, 7, 8, 9, 10]
group2 = [15, 17, 19, 21, 22]
group3 = [30, 32, 35, 37, 40]

f_stat, p_value = anova_test(group1, group2, group3)
print(f"F-statistic: {f_stat}, P-value: {p_value}")