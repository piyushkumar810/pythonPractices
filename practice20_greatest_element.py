# find the greatest element from the list

def greatest_element(list):
    n=len(list)

    greatest=list[0]

    for i in range(1,n):
        if(list[i]>greatest):
            greatest=list[i]
    
    return greatest

list=[2,3,4]
result=greatest_element(list)
print(result)