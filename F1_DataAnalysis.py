import requests
import pandas as pd

url = "https://ergast.com/api/f1/2022/1/results.json"
response = requests.get(url)
data = response.json()
race_results = data["MRData"]["RaceTable"]["Races"][0]["Results"]
df = pd.json_normalize(race_results)
top_five_results = df.loc[:, ["position", "Driver.givenName", "Driver.familyName", "Constructor.name"]]
top_five_results = top_five_results.head(5)
print(top_five_results)
import matplotlib.pyplot as plt

driver_points = df.loc[:, ["Driver.givenName", "Driver.familyName", "points"]]
driver_points = driver_points.sort_values(by="points", ascending=False)

plt.bar(driver_points["Driver.givenName"] + " " + driver_points["Driver.familyName"], driver_points["points"])
plt.xlabel("Driver")
plt.ylabel("Points")
plt.title("Points Earned by Drivers in the 2022 Bahrain Grand Prix")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()