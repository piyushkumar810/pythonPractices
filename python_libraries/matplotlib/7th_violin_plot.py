# ------------------------------------------ Violin plot 
'''
A violin plot is a mix of a box plot and a density plot. It helps us see:

How spread out the data is.
Where most values cluster.
If the data has multiple peaks (different groups).

 Shows the full distribution of data (not just median & quartiles like a box plot).
-> Great for comparing multiple groups (e.g., salaries in different departments).
-> Identifies outliers, peaks, and how values are spread.


example:-
Imagine you are comparing the salaries of employees in different departments:

A box plot will just show the median & range.
A violin plot will show how many employees are in each salary range (thicker parts mean more people).
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate sample data
np.random.seed(10)
data = [np.random.normal(50, 10, 100), np.random.normal(70, 15, 100), np.random.normal(30, 5, 100)]

'''
np.random.seed(10) → Ensures we get the same random data each time we run the program.
np.random.normal(mean, std_dev, size) → Generates 100 random numbers for 3 categories:
Category 1: Mean = 50, Std Dev = 10
Category 2: Mean = 70, Std Dev = 15
Category 3: Mean = 30, Std Dev = 5
This simulates three groups of data with different distributions.
'''

# Create the violin plot
plt.figure(figsize=(8,5))
sns.violinplot(data=data)

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Violin Plot Example")

plt.show()

'''
explanation:-

What Does This Violin Plot Show?
 It compares 3 different groups of data.
 The thicker parts show where most values are concentrated.
 The spread shows how widely values vary.
 Helps in understanding distributions better than box plots.


Where Can You Use This?
-> Comparing salaries in different departments.
-> Comparing exam scores across schools. 
-> Checking product ratings across brands.

'''