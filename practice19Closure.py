x=99
def func1():
    x=88
    def func2():
        print(x)
    func2()
func1()   


# ---------------------------------------------steps-by-step process of execution

# 1. Global Variable Defined: x = 99 is set in the global scope.

# 2. func1() is Called: Execution enters func1.
'''Inside func1, a new local variable x = 88 is created. This x is local to func1 and
    is different from the global x.'''

# 3. func2() is Defined Inside func1:
'''func2 is defined, and it captures x from the enclosing scope of func1.'''
'''However, the code inside func2 does not run yet.'''

# 4. func2() is Called from Inside func1:
'''When func2() is called, it looks for the variable x.'''
'''Since x is not defined in func2 itself, it searches in the enclosing scope (func1) and finds x = 88.'''
'''The print(x) statement inside func2 prints 88.'''


# Q) when func1() start its execution will it go inside funct2() function

'''No, when func1() starts its execution, it will not go inside func2() immediately unless func2()
 is explicitly called. Here's why:'''