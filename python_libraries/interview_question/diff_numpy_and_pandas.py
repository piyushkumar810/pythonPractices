# one difference between numPy and pandas

import pandas as pd
s1=pd.Series(12, index=(1,2,3,4,5,6,7))
s2=pd.Series(12, index=(1,2,3,4))
result=s1+s2

print(result)
print(type(result))

# in pandas --> here you can see it can work with missing data also but,
# in numPy -->  here you will get an error that is :- "broadcast error" (it will not work)