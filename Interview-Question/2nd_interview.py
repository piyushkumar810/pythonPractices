# ----------------------------------- pyhton basic to advanced questions --------------------------------

# Q1) what is pyhton?
'''ans -> python is a versitile and high level programmig language which is known for its simplicity and 
          redability. it is widely used in various domain like web-development , app devlopment
          data analsis, artifical intiligence and so on: 
          it is easy to use.
          interpreted language.
          dynamic typed - means we don't need to declear type of a variable before using it—it can hold values of different types at different times.
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
''' ans -> the loop control statement in python allow you to alter the normal flow of a loop.
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
# join is used when we need to extract data from different dataFrames which  have one or more common columns.

# the stacking is done in a horizontal matter if the join() function is used.

    on → The column or index to join on (only works if df2 has an index).
    how → Type of join ('left', 'right', 'inner', 'outer').

import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'd'])

# Joining DataFrames
result = df1.join(df2)

print(result)
'''

# Q15) which method works best for vertical stacking of DtaFrame?
'''
ans -> the concat() method works best when the dataFrame have the same columns and can be used for concatenation 
       of data having similar fields.
'''

# Q16) how to merge DataFrames in pandas?
'''
merging depends on the type and fields of different DataFrames being merged.

--> if data is having similar fields data is merged along axis 0.
--> if the fields are differnet, they are merged along axis 1.
'''

# Q17) give a DataFrame, how do you drop all rows having NaN ?
'''
the dropna() function in pandas helps to do so
'''

# Q18) how to access the first five and last five entries of a DataFrame ?
'''
for first five --> head(5) function will output the first five entries
for last five --> tail(5) function
'''

# Q19) how to access data from a DataFrame using a value as index ? 
'''
to fetch a new row from DataFrame given index 'x', we use --> loc

# ---------code

import pandas as pd

# Creating a DataFrame with custom index
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35]},
                   index=['a', 'b', 'c'])

# Fetching row where index is 'b'
print(df.loc['b'])

# -----------output
Name    Bob
Age      30
Name: b, dtype: object

'''

# Q20) how do you add single line and multi-line comment in python ?
'''
single line comment --> #

multi-line comment --> ''' ''', """ """
'''


# vvi question
# Q21) what is the most memory-efficient way to add element to a tuple ?
'''
this is a trick qustion because, 
tuples are immutable datatype in python. so you cannot add element to an existing tuple.

--> a new one must be created if the value are to be changed.
'''

# Q22) what is dictionary in python ?
'''
--> a python is a collection of items in no particular order.
--> dictionary are written in curley brackets with key and value pair.

example:- d={"name": "piyush,
             "roll": 28}
'''

# Q23) find out the measure of central tendency for the Numpy array ?
#      np.array([1,5,3,100,4,48])
'''
central tendency means:
function such as mean(), median(), mode()

import numpy as np

data=[1,5,3,100,4,48,4]
print(type(data))

d1=np.array(data)
print(type(d1))

print("mean of the data is ", np.mean(d1))
print("median of the data is ", np.median(d1))
print("mode of the data is ", np.std(d1))
'''

# Q24) what is the use of classifier ?
'''
A classifier in Python is a machine learning model that is used to categorize data into different 
classes (labels). It is a type of supervised learning algorithm that learns patterns from labeled 
data and makes predictions on new data.
'''

# Q25) how do you get a list of all the key in a dictionary ?
'''
while using .keys() function

dict={"a":"piyush",
      "b":28,
      "c":"scooling",
      "d":34}

print(dict.keys())
'''

# Q26) how can you capitalize the first letter of a string ?
'''
using capitalize() function 

string="piyush"
print(string.capitalize())
'''

# Q27) how can you insert an element at a given index in python ?
'''
pyhton has inbuilt function called "insert()"
it can be used to insert an element at any given index

list=[3,5,7,3,7,8,10]
list.insert(6,20)
'''

# Q28) how will you remove duplicate elements from the list ?
'''
the easiest way that you convert your list into set by using set() function, because set doesnot contain 
duplicate value.
after gitting rid of duplicate value again
convert set from list using list() function if requered.

# ------------code
my_list = [1, 4, 7, 1, 3, 6, 4, 1]  # Original list with duplicates
my_list = list(dict.fromkeys(my_list))  # Removing duplicates while maintaining order
print(my_list)  # Output: [1, 4, 7, 3, 6]

# ------------ code for removing duplicates mannualy
list = [1, 4, 7, 1, 3, 6, 4, 1]
unique_list = []
for num in list:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)  # Output: [1, 4, 7, 3, 6]


# ------------- need to know

Which Method is Best?

Method	                      Removes Duplicates	     Preserves Order	        Performance
dict.fromkeys()	                  ✅ Yes                 	✅ Yes	            🚀 Fast
set()	                          ✅ Yes	                    ❌ No	            🚀 Fast
Loop (for + if)                   ✅ Yes	                    ✅ Yes	            🐢 Slow

✅ Best Choice:
Use dict.fromkeys(list) in Python 3.7+ for best performance & order preservation.

'''

# Q29) what is recursion ?
'''
when a function call itself is consider as recursive function.
note:- dont forget to terminate recursion, it will raise problem .
'''

# Q30) explain python list comprehension ?
'''

'''