# ---------------------------closure in python

'''Imagine you’re playing with a box, and inside the box is a special toy. Now, you close the box, 
   but the toy stays inside. You can still carry the box around and play with the toy even though 
   the box is closed. The toy is safe inside and can’t get lost!'''

'''In Python, closures are like this box with the toy inside. The "box" is a function, and the "toy" 
   is a variable inside that function. When you close the box (the function finishes running), 
   the variable doesn’t disappear—it stays hidden inside the box, and you can still use it when you 
   play with the box (call the function again).'''

# eg 
def toy_box(toy):
    def play():
        return f"Playing with {toy}!"
    return play

my_toy = toy_box("car")
print(my_toy()) 

# eg 2

def func1(x):
    def func2(y):
        return x ** y
    return func2

my_result=func1(2)
print(my_result)
print(my_result(2))