import matplotlib.pyplot as plt

# Given data
time = [1, 2, 3, 4, 5, 6]          # time in hours
temperature = [28, 29, 30, 29, 31, 32]  # temperature in °C

# Plot the data
plt.plot(time, temperature)

# Labels and title
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")

# Display the graph
plt.show()
