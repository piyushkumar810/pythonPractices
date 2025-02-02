'''
Stem plot:

A stem plot (or stem-and-leaf plot) is a type of chart that displays data points as vertical stems with markers
at their values. It is similar to a scatter plot but with vertical lines connecting the points to the baseline.

Why Use a Stem Plot?
✅ Good for visualizing small datasets 📊
✅ Shows individual data points clearly 🔍
✅ Easy to compare different values 📈
✅ Highlights trends and patterns in data


'''

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(1, 10, 10)  # X-axis values (1 to 10)
y = np.sin(x)  # Y-axis values (sine function)

# np.linspace(1, 10, 10) → Creates 10 evenly spaced numbers between 1 and 10.
# np.sin(x) → Calculates the sine of each x value.

# Create stem plot
plt.stem(x, y, linefmt="--", markerfmt="D", orientation="vertical")

# Labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Stem Plot Example")

# Show the plot
plt.show()