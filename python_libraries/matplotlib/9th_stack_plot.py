'''
What is a Stack Plot?
A stack plot (or stacked area plot) is used to show multiple data series stacked on top of each other over time. 
It helps in visualizing how different components contribute to the total.

Why Use a Stack Plot?
✅ Shows trends over time 📈
✅ Helps compare multiple categories 🔄
✅ Good for visualizing proportions 🏆
✅ Easy to track total growth 📊
'''

import matplotlib.pyplot as plt
import numpy as np

# Data for years
years = [2018, 2019, 2020, 2021, 2022]

# Data for different categories
category1 = [2, 3, 5, 7, 10]  # Example: Product A sales
category2 = [1, 4, 6, 8, 11]  # Example: Product B sales
category3 = [2, 2, 3, 4, 6]   # Example: Product C sales

# Create stack plot
plt.stackplot(years, category1, category2, category3, labels=["Product A", "Product B", "Product C"], alpha=0.7, baseline="sym")
# baseline:- "sym"-(graph starts from center)


# Labels and title
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Stack Plot Example")

# Add legend
plt.legend()

# Show the plot
plt.show()


'''
    when to use stack plot:

📌 Tracking changes in multiple categories over time (e.g., sales of different products).
📌 Comparing different contributors to a total (e.g., energy consumption from different sources).
📌 Visualizing stacked growth (e.g., company revenue from different regions).
'''