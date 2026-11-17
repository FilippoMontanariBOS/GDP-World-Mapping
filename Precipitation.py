import matplotlib.pyplot as plt
import pandas as pd

df_gdp = pd.read_csv("GDP_data.csv")
df_gdp_fil = df_gdp[['Country Name', '2022']].dropna()

df_prec = pd.read_csv("Prec_data.csv")
df_prec_fil = df_prec[['Country Name', '2022']].dropna()

df_prec_gdp = pd.merge(df_prec_fil, df_gdp_fil, on="Country Name", how="inner")

plt.scatter(df_prec_gdp['2022_x'], df_prec_gdp['2022_y'], color='gray', marker='o', edgecolors='black')
plt.title("Precipitation vs. GDP (2022)")
plt.xlabel("Average Precipitation (mm/yr)")
plt.ylabel("GDP per Capita (Current US$)")
plt.show()