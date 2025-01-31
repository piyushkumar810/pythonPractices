# ------------------------------------ bar chart in matplotlib

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