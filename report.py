import pandas as pd
import matplotlib as ml
from matplotlib import pyplot as plt
ml.style.use('ggplot')

# Create the data
data = [
    ['London', 29.2, 17.4],
    ['Glasgow', 18.8, 11.3],
    ['Capetown', 15.3, 9.0],
    ['Houston', 22.0, 7.8],
    ['Perth', 18.0, 23.7],
    ['San Francisco', 11.4, 33.3]
]

# Create the DataFrame
os_new = pd.DataFrame(data)

# Rename the columns
os_new.rename(columns={0:"Warehouse Location"},inplace=True)
os_new.rename(columns={1:"Profit 2016"},inplace=True)
os_new.rename(columns={2:"Profit 2017"},inplace=True)

os_new.plot(kind="pie",y="Profit 2017")
plt.title('Profit 2017 - Pie Chart')
plt.show()
# Plot line chart
os_new.plot(kind="line", y=["Profit 2016", "Profit 2017"])
plt.title('Profit 2016 vs 2017 - Line Chart')
plt.show()

# Plot area chart
os_new.plot(kind="area", y=["Profit 2016", "Profit 2017"])
plt.title('Profit 2016 vs 2017 - Area Chart')
plt.show()

# Plot bar chart
os_new.plot(kind="bar", y=["Profit 2016", "Profit 2017"])
plt.title('Profit 2016 vs 2017 - Bar Chart')
plt.show()

# Plot horizontal bar chart
os_new.plot(kind="barh", y=["Profit 2016", "Profit 2017"])
plt.title('Profit 2016 vs 2017 - Horizontal Bar Chart')
plt.show()

# Plot scatter chart
os_new.plot(kind="scatter", x="Profit 2016", y="Profit 2017")
plt.title('Profit 2016 vs 2017 - Scatter Plot')
plt.show()

# Plot hexbin chart using matplotlib (instead of pandas' plot)
plt.hexbin(os_new['Profit 2016'], os_new['Profit 2017'], gridsize=20, cmap='Blues')
plt.colorbar(label='Counts')
plt.title('Profit 2016 vs 2017 - Hexbin Plot')
plt.xlabel('Profit 2016')
plt.ylabel('Profit 2017')
plt.show()

