import matplotlib.pyplot as plt
import pandas as pd


df_gdp = pd.read_csv("GDP_data.csv")
years = list(df_gdp.loc[:, '1970':'2025'].columns)
df_gdp_fil = df_gdp[['Country Name'] + years]
df_gdp_ten = (df_gdp_fil[df_gdp_fil['Country Name'].isin(['United States', 'Canada', 'United Kingdom', 'Germany',
             'Italy', 'Denmark', 'Japan', 'India', 'China', 'Australia'])].dropna()).set_index('Country Name')

years_spaced = [int(y) for y in years]

for country in df_gdp_ten.index:
    plt.plot(years_spaced, df_gdp_ten.loc[country], label=country)

plt.xlabel("Year")
plt.ylabel("GDP (USD)")
plt.title("World Economies Over Time")
plt.legend()
plt.show()