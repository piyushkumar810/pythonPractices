# -----------------------------------list in python

a=[3, 28, "piyush" , True, 36.5]
print(a)
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print("\n")

# ---------------------------------list methods in python

# 1st -- insert method
num=[2,5,8,7,3]
print(num)
num.insert(1,"four")
print(num)


# 2nd -- append method
num1=[1,3,5,7,8,"nine"]
print(num1)
num1.append("ten")
print(num1)

# 3rd -- extend method
num2=[1,3,5,7,8,"nine"]
num3=["one","two",3]
print(num2)
print(num3)
num2.extend(num3)
print(num2)

# 4th -- remove method
msg=["hi","piyush","you","are","bad"]
print(msg)
msg.remove("are")
print(msg)

# 5th -- pop method
msg1=["hi","piyush","you","are","bad"]
print(msg1)
msg1.pop()
# you can pass index inside pop method
print(msg1)

# 6th -- del keyword
msg2=["hi","piyush","you","are","bad"]
print(msg2)
del msg2[2]
print(msg2)

# 7th -- clear method
msg3=["hi","piyush","you","are","bad"]
print(msg3)
msg3.clear()
print(msg3)

# 8th -- sort method
msg4=["hi","piyush","you","are","bad"]
print(msg4)
msg4.sort()
print(msg4)

# 9th -- reverse method
msg5=[43,5,76,23,12,23]
print(msg5)
msg5.reverse()
print(msg5)

# 10th -- index method
msg6=["hi","piyush","you","are","bad"]
print(msg6)
msg6.index("piyush")
print(msg6)

# 11th -- count method
msg7=[4,7,2,7,2,5,7]
print(msg7)
msg7.count(7)
print(msg7)

# 12th -- copy method
msg8=["hello", "everyone"]
print(msg8)
msg9=msg8.copy()
print(msg9)