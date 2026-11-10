import matplotlib.pyplot as plt
import pandas as pd

df_gdp = pd.read_csv("GDP_data.csv")
df_gdp_fil = df_gdp[['Country Name', '2022']]

df_prec = pd.read_csv("Prec_data.csv")
df_prec_fil = df_prec[['Country Name', '2022']]

df_prec_gdp = pd.merge(df_prec_fil, df_gdp_fil, on="Country Name", how="inner")

plt.scatter(df_prec_gdp['2022_x'], df_prec_gdp['2022_y'], color='gray', marker='o', edgecolors='black')
plt.title("Precipitation vs. GDP (2022)")
plt.xlabel("Average Precipitation (mm/yr)")
plt.ylabel("GDP per Capita (Current US$)")
plt.show(block=False)

df_gov = pd.read_csv("Gov_Data.csv")
df_gov_fil = df_gov[['Country Name', '2022']]

df_gov_gdp = pd.merge(df_gov_fil, df_gdp_fil, on="Country Name", how="inner")

plt.scatter(df_gov_gdp['2022_x'], df_gov_gdp['2022_y'], color='gray', marker='o', edgecolors='black')
plt.title("Political Stability vs. GDP (2022)")
plt.xlabel("Governance Score (00-100)")
plt.ylabel("GDP per Capita (Current US$)")

plt.show(block=False)

df_edu = pd.read_csv("Education_data.csv")
df_edu_fil = df_edu[['Country Name', '2022']]

df_edu_gdp = pd.merge(df_edu_fil, df_gdp_fil, on="Country Name", how="inner")

plt.scatter(df_edu_gdp['2022_x'], df_edu_gdp['2022_y'], color='gray', marker='o', edgecolors='black')
plt.title("University Education Rate vs. GDP (2022)")
plt.xlabel("University Education Rate (%)")
plt.ylabel("GDP per Capita (Current US$)")
plt.show()