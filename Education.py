import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

df_gdp = pd.read_csv("GDP_data.csv")
df_gdp_fil = df_gdp[['Country Name', '2022']]

df_edu = pd.read_csv("Education_data.csv")
df_edu_fil = df_edu[['Country Name', '2022']]

df_edu_gdp = pd.merge(df_edu_fil, df_gdp_fil, on="Country Name", how="inner")

plt.scatter(df_edu_gdp['2022_x'], df_edu_gdp['2022_y'], color='gray', marker='o', edgecolors='black')
plt.title("University Education Rate vs. GDP (2022)")
plt.xlabel("University Education Rate (%)")
plt.ylabel("GDP per Capita (Current US$)")

'''
slope, intercept, r_value, p_value, std_err = stats.linregress(df_edu_gdp['2022_x'], df_edu_gdp['2022_y'])
r_squared = r_value ** 2

plt.plot(df_edu_gdp['2022_x'], df_edu_gdp['2022_x'] * slope + intercept, color='red')
'''

plt.show()