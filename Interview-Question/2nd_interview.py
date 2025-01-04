# Q1) what is pyhton?
'''ans -> python is a versitile and high level programmig language which is known for its simplicity and 
         redability. it is widely used in various domain llike web- development , app devlopment
         data analsis, artifical intiligence and so on: 
          it is easy to use.
          interpreted language.
          dynamic typed - means we don't need to declear variable explicitly.
          oop feature.
          extensive libraries.'''

# Q2) difference between map and filter?
''' ans -> map -> the map() function is used to apply a specific function to every item in an iterable 
                  (like a list, tuple, or set) and return a map object (an iterator).
                  
                  the function applied to all elements must return a value.
                  
                  here output size is same as the input size.
                  
        filter -> The filter() function in Python is used to filter elements from an iterable based on 
                  a condition specified by a function.
                  
                  the function must return a boolean (True or False).
                  
                  here output size may decreases because of filitration.'''

# Q3) what are loop control statement in python?
''' ans -> the loop control statement in python alloow you to alter the normal flow of a loop.
           there are 3 types of loop control statement in pyhton.
           
           1st -> break statement (exit form the loop permenently if condition met.)
           2nd -> continue statement(skips the current intration and goes to the next iteration.)
           3rd -> pass statement (it does nothing and allows the code to continue running)'''

# Q4) what are keywprds in pyhton?
''' ans -> the keyword are the reversed word which are used as identifiers, function name and more.

           they help define the structure and syntax of the language.

           eg:- False, True, and, if, elif, def, break, continue, return, pass, for etc...'''

# Q5) what are literals in python?
''' ans -> literals in python refers to the data that is given in a vriable or constant.

           there are four types of literals in python: 
           
           1st -> string literal:  sequence of character enclosed within quotes.
           2nd -> numeric literal: integer, float and complex number.
           3rd -> boolean literal: represent True or False.
           4th -> special literal: "None" is a good example.'''

# Q6) how can you concatenate two tuples?
'''sol -> simply we use + (addition symbol)
           eg:-
               tuple1=(1,"piyush", 32.5)
               tuple2=(True, 2, None)

               print(tuple1 + tuple2)  // (1, "piyush", 32.5, True, 2, None)
               print(tuple2 + tuple1)  // (True, 2, None, 1, "piyush", 32.5)''' 

# Q7) how can you initialize a 5*5 NumPy array with only zeros?
''' sol -> NumPy has a brilliant function - zeros() that do this:-

           import numpy as np
           n1= np.zeros((5,5))
           print(n1)                    //  [[0,0,0,0,0]
                                             [0,0,0,0,0]
                                             [0,0,0,0,0]
                                             [0,0,0,0,0]
                                             [0,0,0,0,0]]'''
        
# Q8) what is pandas?
''' ans-> pandas is an open-source library that has a very rich set of data structure for data based
          operation.
          
          pandas can deals with a large varities of files and is one of the most important tools
          to have a grip on.
          
          it provides two fantastic data structure - Series and DataFrames.'''