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
list comphrehension is best way to transform one list into another list.

list comphrehension is generally more compact and faster than normal function or loop for creating list.


example:-
my_list=[10,20,30,40,50]
print(my_list)

new_list=[(x+2) for x in my_list ]
print(new_list)
'''

# Q31) what is the use of bytes() function ?
'''
The bytes() function in Python creates immutable byte sequences. Think of it as a way to store 
binary data (like files, network data, or encrypted messages).

example:- 
b = bytes([65, 66, 67])
print(b)  # Output: b'ABC'
'''

# Q32) what is 'with statement' used for in python ?
'''
The with statement in Python is used to handle resources like files, network connections, 
and database connections efficiently. It ensures that resources are automatically closed 
after they are used, even if an error occurs.

Why Use with?
✅ Avoids manual closing of resources
✅ Prevents memory leaks
✅ Makes code cleaner & readable


# ---------Example: Using with for File Handling
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Reads and prints the file content
# File automatically closes after this block


# ----------Without with, you would have to write:
file = open("example.txt", "r")
content = file.read()
file.close()  # Must be done manually
'''

# Q33) what is a map() function in python ?
'''
a map function in python is used for appling a function on all elements of a specific iterable

--> it consist of two parameters, function and iterable (it can be list, tuple, anything..)

example:- 
def cube(x):
    return x*x*x

list1=[3,5,6,2,8,9,11]
# list2=map(cube,list1) #it will return object you will have to convert it into list
list2=list(map(cube,list1))
print(list2)  # output [27, 125, 216, 8, 512, 729, 1331]
'''

# Q34) what is __init__ in python ?
'''
--> the __init__ method is a reserved method in python.
--> it is also known as constructor in the world of oops.
--> when an object of class is created, the __init__ method is automatically 
    called to access the class attributes.
'''

# Q35) what are the tools present to perform 'static analysis' ?
'''
static analysis tools are use to find bugs in python progam :- 

there are two static analysis tools:
1st--> pychecker (detects bugs from source code and warns about its style and complexity.)
2nd--> pylint (checks whether the module matches up to a set coding standareed or not)
'''

# Q36) what is the difference between a tuple and a dictionary ?
'''
Tuple vs Dictionary in Python

Feature	                Tuple (tuple)	                                    Dictionary (dict)
----------       -------------------------------                     ----------------------------------
Definition	     An ordered collection of elements	                 A key-value pair collection
Mutability	     Immutable (cannot be changed after creation)	     Mutable (values can be changed)
Indexing	     Indexed by position (e.g., tuple[0])	             Indexed by keys (e.g., dict["name"])
Duplicates	     Can have duplicate values	                         Keys must be unique, but values can be duplicated
Performance      Faster (due to immutability)	                     Slightly slower (due to key lookup)

'''

# Q37) what is pass in python ?
'''
The pass statement in Python is a placeholder that does nothing when executed.
the function, class and loop uses pass it means that it will defined later.
--> is the statement ignored by the interpreter?
    no this statement is not ignored by the interpreter.

example: 

# ------------------- empty function placeholder
def my_function():
    pass  # To be implemented later

print("Function defined successfully!")


# ------------------- empty class placeholder
class MyClass:
    pass  # Will add methods later


# ------------------- using pass in loops
for i in range(5):
    if i == 2:
        pass  # Skip execution but avoid syntax errors
    else:
        print(i)
'''

# Q38) how can an object be copid in python ?
'''
not all object can be copid in python, but most can.

In Python, objects can be copied using different methods depending on whether you need a shallow copy or a deep copy.

1️⃣ Shallow Copy (copy.copy())
🔹 Creates a new object but keeps references to nested objects

----example: -
import copy

original = [1, [2, 3], 4]
shallow_copy = copy.copy(original)

shallow_copy[1][0] = 99  # Modifies the original object too!

print(original)       # Output: [1, [99, 3], 4]
print(shallow_copy)   # Output: [1, [99, 3], 4]


2️⃣ Deep Copy (copy.deepcopy())
🔹 Creates a completely independent copy, including nested objects

------- example :-
import copy

original = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original)

deep_copy[1][0] = 99  # Does NOT affect the original!

print(original)      # Output: [1, [2, 3], 4]
print(deep_copy)     # Output: [1, [99, 3], 4]


note:- Immutable objects (int, str, tuple) don’t need copying since they can't be changed.
'''

# Q39) how can a number be converted to a string ? 
'''
the inbuilt function "str()" can be used to convert a number to a string

example: -
n=10
print(type(n))
new_n=str(n)
print(type(new_n))
'''

# Q40) what are modules and packages in python ?
'''
Feature	                    Module	                                          Package
--------              -----------------------                        ----------------------------
What is it?	          A single Python file (.py)	                 A folder containing multiple modules
Purpose	              Stores related functions & classes	         Groups related modules together
Example	              math.py	                                     numpy, pandas (which have many modules inside)
Import	              import module_name	                         from package_name import module_name

real life example :
Think of modules as books 📖 and packages as a library 📚.

A module (math.py) is one book with formulas.
A package (numpy) is a library with multiple books (modules) on mathematics.
'''