'''This chi2_square test is the one of the valuable method for analyzing
 categorical data and assessing relationships between categorical variables'''
import numpy as np
from scipy.stats import chi2_contingency

# contigency table
data = np.array( [[10, 15, 5], # category A
                  [5, 10, 20], # Category B
                  [15, 5, 10]]) # Category

# perform the Chi_Square test
chi2_stat, p_val, dof, exptected = chi2_contingency(data)

print(f"Chi_Square Statistic:{chi2_stat}")
print(f"P.value:{p_val}")
print(f"Degrees of Freedom:{dof}")
print(f"Expected Frequencies:")
print(exptected)

