import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

# world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
world = gpd.read_file("data/world-administrative-boundaries/world-administrative-boundaries.shp")
smoker_data = pd.read_csv("data/daily-smoking-prevalence-bounds.csv")
smoker_data = smoker_data[smoker_data["Year"] == 2012]

merged = world.set_index("iso3").join(smoker_data.set_index("Code"))

fig, ax = plt.subplots(1, 1, figsize=(18, 12))
merged.plot(column="Daily smoking prevalence", cmap="OrRd", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True, missing_kwds={'color': 'lightgrey'})
ax.set_title("Share of people who smoke daily")
plt.yticks([])
plt.xticks([])
plt.tick_params(axis='both', which='both', length=0)
fig.text(1.15, 0.5, "Prevalence of daily smokers (%)", fontsize=12, va='center', ha="left", rotation="vertical", transform=ax.transAxes)
ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='No Data', markersize=10, markerfacecolor='lightgrey')])
plt.show()
