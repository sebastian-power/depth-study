# import geopandas as gpd
# ^ line only needed if making map
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from corrpy import corrcheck

respiratory_data = pd.read_csv("data/less_data.csv")
co2_data = pd.read_csv("data/co2-data.csv")

merged = pd.merge(respiratory_data, co2_data, on="iso_code")
np.set_printoptions(suppress=True)
x = np.array(merged["Percentage of cause-specific deaths out of total deaths"])
y = np.array(merged["co2"])

valid_indices = np.logical_and(~np.isnan(x), ~np.isnan(y))
x = x[valid_indices]
y = y[valid_indices]

plt.scatter(x, y, label="Data points")
plt.yscale("log")
plt.xscale("log")
print(f"X: {x}")
print(f"Y: {y}")
m, b = np.polyfit(np.log(x), np.log(y), 1)
print(f"M: {m}")
print(f"B: {b}")
print(f"X_FIT: {x}")
y_fit = np.exp(m * np.log(x) + b)
print(f"Y_FIT: {y_fit}")
plt.plot(x, y_fit, color="red")
print(corrcheck(x,y))
plt.xlabel("Percentage of respiratory disease deaths out of total deaths")
plt.ylabel("CO2 levels")
plt.title("Respiratory disease deaths vs CO2 levels")
plt.legend()
plt.show()


# world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
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
