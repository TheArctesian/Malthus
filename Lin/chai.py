import pandas as pd
import researchpy as rp
import scipy.stats as stats

df = pd.read_csv('lin.csv')

crosstab = pd.crosstab(df["log"], df["pred"])
print(crosstab)
print(stats.chi2_contingency(crosstab)[0:3])
