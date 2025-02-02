'''
? What is a Subplot?
"A subplot in Matplotlib allows you to display multiple plots within a single figure". 
It helps compare different datasets or visualize multiple aspects of the same data in one view.

'''

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# First subplot
plt.subplot(2, 1, 1)  # (rows, columns, index)
plt.plot(x, y1, color="r", label="Sine Wave")
plt.title("Sine Wave")
plt.legend()

# Second subplot
plt.subplot(2, 1, 2)
plt.plot(x, y2, color="b", label="Cosine Wave")
plt.title("Cosine Wave")
plt.suptitle("Trignometric functions")
plt.legend()

'''
Explanation of plt.subplot(2, 1, 1)
(rows, columns, chart number)

2, 1 → 2 rows, 1 column (stacked vertically).
1 → First subplot (Sine Wave).
2 → Second subplot (Cosine Wave).

'''

plt.tight_layout()  # Adjust spacing
plt.show()



# ----------------------------------------- explained linespac() function of numpy

'''
The numpy.linspace() function generates evenly spaced numbers over a specified range. 
    It is useful for creating smooth curves in graphs.

    its attributes: 
        start: The starting value of the sequence.
        stop: The ending value of the sequence.
        num: The number of points to generate (default = 50).
        endpoint: If True, includes the stop value; if False, excludes it.

example:- 
x = np.linspace(0, 10, 100)
start = 0, stop = 10, num = 100 → Generates 100 evenly spaced numbers between 0 and 10.

The values of x look like:
[0.0, 0.101, 0.202, 0.303, ..., 9.899, 10.0]

This creates a smooth curve when plotting sin(x) and cos(x), instead of jagged points

Example of linespace:-

# import numpy as np
# import matplotlib.pyplot as plt

# x1 = np.linspace(0, 10, 5)   # Only 5 points (less smooth)
# x2 = np.linspace(0, 10, 50)  # 50 points (smoother)
# x3 = np.linspace(0, 10, 100) # 100 points (very smooth)

# plt.plot(x1, np.sin(x1), 'o-', label="5 points")
# plt.plot(x2, np.sin(x2), 's-', label="50 points")
# plt.plot(x3, np.sin(x3), 'd-', label="100 points")

# plt.legend()
# plt.show()
'''
