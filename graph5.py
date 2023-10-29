import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

air_data = pd.read_csv("data/worldbank/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5994720.csv")

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
merged = world.set_index("iso_a3").join(air_data.set_index("iso_code"))
fig, ax = plt.subplots(1, 1, figsize=(18, 12))
merged.plot(column="2014", cmap="OrRd", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True, missing_kwds={'color': 'lightgrey'})
ax.set_title("GDP per capita by Country")
plt.yticks([])
plt.xticks([])
plt.tick_params(axis='both', which='both', length=0)
fig.text(1.15, 0.5, "GDP per capita ($USD)", fontsize=12, va='center', ha="left", rotation="vertical", transform=ax.transAxes)
ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='No Data', markersize=10, markerfacecolor='lightgrey')])
plt.show()
