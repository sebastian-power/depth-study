import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
respiratory_data = pd.read_csv("data/less_data.csv")
co2_data = pd.read_csv("data/co2-data.csv")

merged = pd.merge(respiratory_data, co2_data, on="")
plt.scatter(co2_data)

# merged = world.set_index("iso_a3").join(respiratory_data.set_index("Country Code"))

# fig, ax = plt.subplots(1, 1, figsize=(18, 12))
# merged.plot(column="Percentage of cause-specific deaths out of total deaths", cmap="OrRd", linewidth=0.8, ax=ax, edgecolor="0.8", legend=True, missing_kwds={'color': 'lightgrey'})
# ax.set_title("Respiratory Disease Deaths by Country")
# plt.yticks([])
# plt.xticks([])
# plt.tick_params(axis='both', which='both', length=0)
# fig.text(1.15, 0.5, "Percentage of Respiratory Disease deaths out of total deaths", fontsize=12, va='center', ha="left", rotation="vertical", transform=ax.transAxes)
# ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='No Data', markersize=10, markerfacecolor='lightgrey')])
# plt.show()
