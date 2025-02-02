# box plot --> A box plot (also called a box-and-whisker plot) is a statistical chart that visually 
               # represents the distribution of a dataset. It helps identify median, quartiles, outliers, 
               # and spread of the data.

# example:- 

import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [12, 15, 14, 10, 18, 21, 22, 23, 25, 30, 35, 40, 50]
data1=[1,2,4,6,9,12,3,2,24]

plot_values=(data,data1)

# Creating a box plot
plt.boxplot(plot_values, vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# Labels and title
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.title("Box Plot Example")

plt.show()