# ----------------------------------- pyhton basic to advanced questions --------------------------------

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


# Q4) what are keywords in pyhton?
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
'''
•	It is one of the most important python library that is used for data analysis.
•	It was created by wes mckinney in 2008.
•	It has functions for analyzing, cleaning, exploring and manipulating data.
•	It can read and data structure of different formats like:- csv, Json, zip, text, xml etc.(matlab Kisi v file formate k saath kam ker Sakata hai).
'''

# Q9) what are dataFrames?
'''
dataFrames are two-dimensional, tabular data structure, similar to the spreadsheet or sql table, it consists of row 
and columns where each column holds the data of the specific type(eg:- integer, float, string).

it is mutable.
you ca store hetrogeneous data. 
it is widely used for data manipulation and analysis in python.
'''

# Q10) what are panda series?
'''
series is one-deminational pandas data structure that supports data of almost any type.

interviewer can ask is'at series inafficient?
ans--> no we cannot say ti is inafficient because if my project requires working of single-dimenational data 
structure the why i will complicate with dataFrame insted i will use series.
'''

# Q11) what is the use of pandas "groupby()" function?
'''
groupby() is a feature supported by pandas which is used to split and group an object.

like the sql, Mysql and oracal groupby, it is used to group the data by classes and entities which can be further 
used for aggregation.

ex:- 

import pandas as pd
x=pd.DataFrame({'vechicle': ['kia', 'lamborghini', 'ktm', 'pulsar200' ,'lexes', 'tata safari'],
                'type':['car', 'car', 'bike', 'bike', 'car', 'car']})
print(x)
print(type(x))
print("\n")
count_of_total=x.groupby('type').count()
print(count_of_total)

'''

# Q12) how to create a dataFrame from a lists?
'''
import pandas as pd

# 1st create an empty dataFrame 
x=pd.DataFrame()

# this are the lists data which we have to convert into dataFrame
bikes=['bajaj', 'tvs', 'honda', 'kawasaki', 'bmw']
cars=['lamborghini', 'masserati', 'hyundai', 'ford', 'farreri']

# 2nd addition of lists as individual columns in the dataFrame
x['bikes']=bikes
x['cars']=cars

print(x)
print(type(x))

'''

# Q13) how to create dataFrame from dictionary?
'''
# the dictionary cann be directly passed as an argument to the dataframe() function to create dataFrame.

import pandas as pd

bikes=['bajaj', 'tvs', 'honda', 'kawasaki', 'bmw']
cars=['lamborghini', 'masserati', 'hyundai', 'ford', 'farreri']

d={"cars":cars, 'bikes':bikes}

x=pd.DataFrame(d)

print(x)
print(type(x))

'''

# Q14) how to combine the dataFrames using "join()" function?
'''
join is used when we need to extract data from different dataFrames which 
''' 
import pandas as pd

x1=pd.DataFrame({})