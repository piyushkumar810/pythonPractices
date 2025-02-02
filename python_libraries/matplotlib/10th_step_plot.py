'''
What is a Step Plot?
A step plot is a type of line plot where data points are connected using steps instead of straight lines. It is useful for showing changes at discrete intervals rather than continuous trends.

Why Use a Step Plot?
✅ Good for visualizing stock prices, event-based data, or digital signals 📊
✅ Shows how values change at specific points in time ⏳
✅ Useful for tracking sudden changes in data 🔄
✅ Clear representation of stepwise changes 🚶‍♂️
'''

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([10, 15, 12, 18, 20, 22, 19, 25])

# Create step plot
plt.step(x, y, where='mid', color='b', linestyle='-', marker='o', label="Sales Over Time")

'''
plt.step(x, y, where='mid') → Creates a step plot.

where='mid' → Steps are centered in the middle of each interval.
              Other options:
              'pre' → Step moves before the point.
              'post' → Step moves after the point.
'''

# Labels and title
plt.xlabel("Time (Months)")
plt.ylabel("Sales")
plt.title("Step Plot Example")

# Add legend
plt.legend()

# Show the plot
plt.show()
