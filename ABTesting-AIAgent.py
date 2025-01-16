import numpy as np
from scipy import stats

class DataPreparationAgent:
    def clean_data(self, data):
        # Implement data cleaning steps
        pass

    def split_data(self, data, test_size=0.2):
        # Implement data splitting steps
        pass

class StatisticalTestAgent:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def t_test(self, sample1, sample2):
        t_stat, p_value = stats.ttest_ind(sample1, sample2)
        return t_stat, p_value

    def anova_test(self, *samples):
        f_stat, p_value = stats.f_oneway(*samples)
        return f_stat, p_value

class SignificanceEvaluationAgent:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def check_significance(self, p_value):
        if p_value <= self.alpha:
            return "Reject the null hypothesis: There is a significant difference."
        else:
            return "Fail to reject the null hypothesis: No significant difference."