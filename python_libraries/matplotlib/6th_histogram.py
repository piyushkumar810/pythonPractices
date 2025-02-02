# Histogram:-  A histogram is a type of bar chart that represents the distribution of numerical data by
                #  grouping values into ranges (bins) and displaying the frequency of occurrences in each range.

import matplotlib.pyplot as plt

ages = [22, 25, 28, 30, 32, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75]
plt.hist(ages, bins=5, color="blue", edgecolor="black")

# what does bin means
# bins=5 → Divides the age range into 5 groups (bins). 
'''
explanation:

X-axis (Age Groups): Divides ages into 5 bins (e.g., 20-30, 30-40, etc.).
Y-axis (Frequency): Shows how many people fall into each bin.
The tallest bar represents the most common age group.


Expected Output:

A histogram with 5 bars, each showing the frequency of people in that age range.
For example, if ages 22, 25, 28, and 30 fall into the same bin, that bar's height will be 4.
'''

plt.xlabel("Age Groups")
plt.ylabel("Frequency")
plt.title("Age Distribution Histogram")

plt.show()