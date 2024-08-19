# removing zero from list and add zero to the last index of the list, the list item should be int type only

list =[2,5,0,4,0,6,8,7]
for i in list:
    if i==0:
        list.remove(i)
        list.append(i)
print(list)