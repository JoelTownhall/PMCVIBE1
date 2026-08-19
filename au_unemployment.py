"""Plot Australia's latest unemployment rate from the ABS Data API."""
import pandas as pd
import matplotlib.pyplot as plt
#bnvvvjfgfhgfghfh
# test
URL = "https://data.api.abs.gov.au/rest/data/ABS,LF,1.0.0/M13.3.1599.20.AUS.M?startPeriod=2015-01&format=csv"

df = pd.read_csv(URL, usecols=["TIME_PERIOD", "OBS_VALUE"]).sort_values("TIME_PERIOD")
df["TIME_PERIOD"] = pd.to_datetime(df["TIME_PERIOD"])

# Build and save a line chart of the unemployment rate over time
plt.plot(df["TIME_PERIOD"], df["OBS_VALUE"])
plt.title("Australia Unemployment Rate (Seasonally Adjusted)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("au_unemployment_rate.png")
plt.show()
