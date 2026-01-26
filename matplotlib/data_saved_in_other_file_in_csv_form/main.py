import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\pythonPractices\matplotlib\data_saved_in_other_file_in_csv_form\temprature.csv")

# Extract columns
time = data["time"]
print(type(time))
temperature = data["temperature"]

# Plot the data
plt.plot(time, temperature)

# Labels and title
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")

# Show the graph
plt.show()
