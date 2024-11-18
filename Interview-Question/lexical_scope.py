def outer_function(x):  # x belongs to the enclosing scope
    def inner_function(y):  # y is in the local scope of `inner_function`
        return x + y  # x is remembered from the enclosing scope
    return inner_function

closure = outer_function(10)  # x = 10
print(closure(5))  # y = 5, Output: 15

'''The function inner_function can still use x from outer_function even after outer_function 
   has finished. This happens because x was in the scope of inner_function when it was written, 
   and this relationship is remembered (not based on when inner_function is called). 
   That’s lexical scope!'''