# ------------------------------------ bar chart in matplotlib
'''
A bar plot (bar chart) represents categorical data using rectangular bars.

When to Use a Bar Plot?
✅ Categorical data (e.g., brands, departments, age groups).
✅ Comparison between different categories.
✅ Emphasizing differences between values.

'''

import matplotlib.pyplot as plt

y=[98,67,88,95,88,46,79,95]
x=["part1","part2","part3","part4","part5","part6","part7.1","part7.2"]

# if you want to assign each bar graph with different color
color=["red", "green", "blue", "pink", "black", "gray", "yellow", "brown"]

# it will plot x and y axis on bar graph
plt.bar(x,y, color=color)

# if you want to give anything in x axis and y axis (use xlabel nad ylabel)
plt.xlabel("parts of harry potter",fontsize=15)
plt.ylabel("popularity", fontsize=15)

plt.title("popularity of differente parts of harry potter",fontsize=17)

# it will show the output on white screen
plt.show()


# --------------------------------------- grouped bar chart
import numpy as np

brands = ["OnePlus", "Apple", "Vivo", "Redmi", "Samsung"]
users_2023 = [13, 25, 22, 18, 22]
users_2024 = [15, 28, 20, 19, 25]

x = np.arange(len(brands))  # Positions for bars

plt.bar(x - 0.2, users_2023, width=0.4, label="2023", color="blue")
plt.bar(x + 0.2, users_2024, width=0.4, label="2024", color="red")

plt.xticks(x, brands)  # Set category labels

plt.xlabel("Brands")
plt.ylabel("Number of Users")
plt.title("Mobile Phone Users Comparison (2023 vs 2024)")
plt.legend()
plt.show()
