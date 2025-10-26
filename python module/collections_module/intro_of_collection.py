# what are collections in python?
'''
collection in python basically contains data type namilly (list, tuples, sets, dictionary)

collection also comes with built in module in python.
collection built in module inplements specialised collection data structure.

'''

# some of the  specialised collection data types are:-
'''
namedtuple()
Chainmap
deque
Counter
OrderedDict
defaultdict
UserDict
UserList
UserString
'''

# 1. namedtuple()
'''
it returns a tuple with a named value for each element in the tuple.
'''

from collections import namedtuple
print("----------- working with namedtuple()---------------")
a=namedtuple('courses','name,technology')
s=a('data science','python')
s1=a._make(['aritificial intelligence', 'python'])
print(s)
print(s1)

# 2. deque
'''
it is used to perform insertion and deletion easily.
'''
print()
print("------------- working with deque-------------")
from collections import deque
lst=[1,2,3,'a','b','c','aaryan']
dq=deque(lst)
print(dq)
dq.append("piyush")
print(dq)
dq.appendleft(42.5)
print(dq)
dq.insert(3,'hello')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.count(lst)
print(f"this is count {dq}")


# 3. Chainmap
'''
chainmap is a dictionary like class for creating a single view of multiple mapping
'''
from collections import ChainMap
print()
print("------------ working with chainmap----------")
a1={1:'edureka',2:'python'}
b1={3:'ml',4:'ai'}
res=ChainMap(a1,b1)
print(res)

# 4. Counter
'''
counter is a dictionary subclass for counting hashable objects
'''
from collections import Counter
print()
print("--------------working with counter--------------")
a2=[1,1,1.5,2,1,5,6,8,0,3,6,8,9,5,3,2,1.4,1.5,2,2,0,2,4,5,7,8,9,3]
res2=Counter(a2)
print(res2)
print(res2.most_common())
sub={2:1,7:1}
print(res2.subtract(sub))
print(res2)

# 5. OrderdDict
'''
ordereddict is a dictionary subclass which remembers the order in which the entries were done
'''
from collections import OrderedDict
print()
print("-------------- working with ordereddict-------------")
d=OrderedDict()
d[1]='d'
d[2]='r'
d[3]='z'
d[4]='q'
d[5]='p'
d[6]='i'
d[7]='y'

print(d)

# 6. defaultdict
'''
ordereddict is a dictionary subclass which calls a factory function to supply missing value
'''
from collections import defaultdict
print()
print("-------------- working with defaultdict-------------")
dict1=defaultdict(int)
dict1[1]='python'
dict1[2]="java"

print(dict1[3])
# note but when you wwork with normal dictionary you will get the keyerror but here you not get any error

#7--------------------- userDict, UserList,UserString--------------------------
'''
userDict- wraps around dictionary object for easier dictionary  sub-class.
userList- this class acts like wrapper around the list objects for easier list sub-classing.
userstring- this also acts like wrapper around the string objects for easier string sub-classing.
'''
print()

