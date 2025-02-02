import matplotlib.pyplot as plt

x=[5,7,3,4,9,10,12]
y=[7,8,4,3,2,15,16]
# z=[1,2,6,7,9,0,2,3]

'''
----------------- error occured

1️⃣ Data Length Mismatch in z

z has 8 elements, while x and y have 7 elements.
This will cause an error when plotting y vs z.
✅ Fix: Ensure z has 7 elements.
'''
z=[1,2,6,7,9,0,2]
a=[3,4,5,6,7,8,8]

plt.figure(figsize=[7,3])
plt.plot(x,y, label="male")
plt.plot(x,z, label="female")
plt.plot(x,a, label="female")

plt.legend(loc=0)
# # loc= (gooes to 0-9, by default it is loc=0, and by default it is in perfect place)

# # you can also change the name of the labels
# plt.legend(["a1", "a2"])

# # by default the legends will be displayed in rows but if you want it in columns
# plt.legend(["a1", "a2"], ncols=2)

# # if you want the label to be displayed out of the box 
# plt.legend(bbox_to_anchor=(0.8, 1.2), ncols=2, labelspacing=2)

plt.show()