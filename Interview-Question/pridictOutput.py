
#----------------------------------------------------- what will be the output

#  ----------------------q1
# print("hello{0[0]} and {0[1]}".format(('PW', 'Learner')))

# Explanation
# The format() method takes a tuple ('PW', 'Learner') as its argument.
# The {0[0]} and {0[1]} syntax means:
# 0 refers to the first positional argument (the tuple).
# [0] and [1] index the tuple to access its first and second elements, respectively.
# As a result, this code outputs:
#                                helloPW and Learner


# -----------------------q2
# num2=int(input("num2= "))
# print(num1/num2)

# sol--> runtime error

# ------------------------q3
# a=8
# b=4
# print(a|b)
# print(a>>2)

# Explanation
# a | b (Bitwise OR):
# a = 8 (binary: 1000)
# b = 4 (binary: 0100)
# Bitwise OR operation combines bits: 1000 | 0100 = 1100 (binary), which is 12 in decimal.
# So, print(a | b) outputs 12.

# a >> 2 (Right Shift):
# a = 8 (binary: 1000)
# Right shift by 2 moves bits 2 places to the right: 0010 (binary), which is 2 in decimal.
# So, print(a >> 2) outputs 2.

# -----------------------------q4
x=9
y=41

print(x or y, x and y) 
print(x|y , x&y)
print("\n")

# ---------------------------q5
print(7//2)
print(-7//2)

# ----------------------------q6
print("the banana tree said",",""I'm",1200,"year old.")