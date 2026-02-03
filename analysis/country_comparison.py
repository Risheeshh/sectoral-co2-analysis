import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("co2_emissions.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
df["year"] = df["date"].dt.year
df = df.rename(columns={"value": "co2_emissions"})
df = df.dropna(subset=["year", "co2_emissions"])

latest_year = df["year"].max()
latest_data = df[df["year"] == latest_year]

top_countries = (
    latest_data.groupby("country")["co2_emissions"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index
)

filtered = latest_data[latest_data["country"].isin(top_countries)]

country_sector = (
    filtered.groupby(["country", "sector"])["co2_emissions"]
    .sum()
    .reset_index()
)

plt.figure()
for country in country_sector["country"].unique():
    data = country_sector[country_sector["country"] == country]
    plt.bar(data["sector"], data["co2_emissions"], label=country)

plt.xlabel("Sector")
plt.ylabel("CO₂ Emissions")
plt.title(f"Sector-wise CO₂ Emissions by Country ({latest_year})")
plt.legend()
plt.savefig("figures/country_comparison.png", dpi=300, bbox_inches="tight")
plt.close()
