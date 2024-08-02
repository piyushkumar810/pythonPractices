# ----------------------------------break and continue statement in python

# Q1) for break statement : - break the loop
for i in range(20):
    print(i)
    if(i==15):
        print("now i is greater than ", i)
        break
        print("exit from loop")

# Q2)for continue statement :- break the iteration
for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    
    print("5 * ",i, "=", 5*i)