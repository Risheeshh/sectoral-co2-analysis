import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("co2_emissions.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
df["year"] = df["date"].dt.year
df = df.rename(columns={"value": "co2_emissions"})
df = df.dropna(subset=["co2_emissions"])

sector_share = df.groupby("sector")["co2_emissions"].sum()

plt.figure()
plt.pie(sector_share, labels=sector_share.index, autopct="%1.1f%%")
plt.title("Overall Sectoral Contribution to CO₂ Emissions")
plt.savefig("figures/sector_share.png", dpi=300, bbox_inches="tight")
plt.close()
