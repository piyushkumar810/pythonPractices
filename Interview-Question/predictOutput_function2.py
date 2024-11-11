def outer_function(a,b):
    def inner_function(c,d):
        c,d=d,c
        return c-d
    
    return inner_function(a,b)
    return a

result=outer_function(5,10)
print(result)



# ------------------------------------------------expalnation-----------------------------------------

# 1. What is a function?
'''A function is like a little machine where you put something in (input), and it gives you something 
back (output). In this case, outer_function and inner_function are both little machines.'''

# 2. The Outer Function:
'''In your code, outer_function(a, b) is the first machine that takes in two things: a and b. In the
 example call, a = 5 and b = 10.'''

# 3. The Inner Function:
'''Inside the outer function, there is another machine called inner_function(c, d). This inner machine 
gets two new things: c and d. These two values are swapped around, and then c - d is calculated
and returned.'''

# 4. What Happens Step-by-Step?
# First, outer_function(5, 10) is called. The a = 5 and b = 10 are passed to the outer machine.

# Inside the outer machine, it calls the inner machine (inner_function) with a and b, which means c = 5 and d = 10 inside the inner machine.

# In the inner machine, the values of c and d are swapped, so now c = 10 and d = 5.

# The inner machine calculates c - d, which is 10 - 5 = 5, and returns that result (5).
# Now, outer_function takes that result from the inner machine (which is 5) and gives it back as the final result.

# 5. The Extra return a:
'''There's a second return a after the inner function. This will never be executed!
The reason is that the first return in the function sends the result back to where the function was
called. Once the function has returned something, the rest of the code is ignored, so the second 
return a doesn't do anything.'''