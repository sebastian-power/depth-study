import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from corrpy import corrcheck

respiratory_data = pd.read_csv("data/who_respiratory_data.csv", index_col=False)
co2_data = pd.read_csv("data/trimmed_co2_data.csv")

pop_change = [int(cent["population"]) for index, cent in co2_data.iterrows() if cent["year"] == 2019]
pop_change2 = [int(cent["population"]) for index, cent in co2_data.iterrows() if cent["year"] == 2000]
dis_change = [int(cent["Total"]) for index, cent in respiratory_data.iterrows() if cent["Year"] == 2019]
dis_change2 = [int(cent["Total"]) for index, cent in respiratory_data.iterrows() if cent["Year"] == 2000]
co2_change = [int(cent["co2"]) for index, cent in co2_data.iterrows() if cent["year"] == 2019]
co2_change2 = [int(cent["co2"]) for index, cent in co2_data.iterrows() if cent["year"] == 2000]
disease_prevalence = [cent["Total"] for index, cent in respiratory_data.iterrows()]
co2_levels = [cent["co2"] for index, cent in co2_data.iterrows()]
x = np.arange(2000,2020)
a,b = np.polyfit(x, np.array(disease_prevalence), 1)
print(corrcheck(disease_prevalence, co2_levels))
fig, ax1 = plt.subplots()
ax1.set_ylabel("CO2 levels(million tonnes)")
ax1.set_xlabel("Year")
ax1.plot(x, co2_levels, label="CO2 levels", color="tab:red")
# ax1.plot(x, co2_levels, label="CO2 levels", color="tab:red")
ax1.legend()
ax1.tick_params(axis='y', labelcolor='tab:red')
ax2 = ax1.twinx()
ax2.scatter(x,disease_prevalence, color="tab:blue")
ax2.plot(x, a*np.array(x)+b, label="Disease Deaths")
ax2.legend(loc="lower right")
ax2.set_ylabel("Respiratory Diseases Deaths")
plt.title("Deaths by Respiratory Diseases in Australia vs CO2 levels in Australia")
print(f"Population % change: {round(((pop_change[0] - pop_change2[0])/pop_change2[0])*100, 2)}")
print(f"Respiratory disease prevalence % change: {round(((dis_change[0] - dis_change2[0])/dis_change2[0])*100, 2)}")
print(round(((co2_change[0] - co2_change2[0])/co2_change2[0])*100, 2))
plt.show()
