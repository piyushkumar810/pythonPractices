def safe_access(lst, index):
    try:
        result=lst[index]
    except IndexError:
        print("index out of bound")

lst=[10,20,30]
index=int(input("enter the eindex"))
print(safe_access(lst,index))
