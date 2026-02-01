
n=int(input("enter the row "))
for i in range(1,n+1):
    spaces=(n-i)
    star=(2*i-1)
    print(" "*spaces + "*"*star)