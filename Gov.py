import matplotlib.pyplot as plt
import pandas as pd

year = '2022'
df_gdp = pd.read_csv("GDP_data.csv")
df_gdp_fil = df_gdp[['Country Name', year]].dropna()

df_gov = pd.read_csv("Gov_Data.csv")
df_gov_fil = df_gov[['Country Name', year]].dropna()


df_gov_gdp = pd.merge(df_gov_fil, df_gdp_fil, on="Country Name", how="inner")

plt.scatter(df_gov_gdp['2022_x'], df_gov_gdp['2022_y'], color='gray', marker='o', edgecolors='black')
plt.title("Political Stability vs. GDP (2022)")
plt.xlabel("Governance Score (00-100)")
plt.ylabel("GDP per Capita (Current US$)")

plt.show()