import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("co2_emissions.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
df["year"] = df["date"].dt.year
df = df.rename(columns={"value": "co2_emissions"})
df = df.dropna(subset=["year", "co2_emissions"])

sector_trend = (
    df.groupby(["year", "sector"])["co2_emissions"]
    .sum()
    .reset_index()
)

plt.figure()
for sector in sector_trend["sector"].unique():
    data = sector_trend[sector_trend["sector"] == sector]
    plt.plot(data["year"], data["co2_emissions"], label=sector)

plt.xlabel("Year")
plt.ylabel("CO₂ Emissions")
plt.title("Sector-wise CO₂ Emission Trends Over Time")
plt.legend()
plt.savefig("figures/sector_trends.png", dpi=300, bbox_inches="tight")
plt.close()
