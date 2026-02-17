# Write a Python program using procedural approach to:
#    Accept a range
#    Print numbers where sum of digits is divisible by 3
#    Count how many such numbers exist

def sum_of_digits(num):
    s=0
    while(num>0):
        rem=num%10
        num=num//10
        s=s+rem
    return s

def main_op():
    start=int(input("enter the starting range: "))
    end=int(input("enter the ending range: "))

    count=0
    for i in range(start,end+1):
        num1=sum_of_digits(i)
        if(num1%3==0):
            count=count+1
            print(i)

    print(f"total {count} no exists")
main_op()


# print(sum_of_digits(5))
# print(sum_of_digits(15))

'''
s="pif"
print(len(s))

s=1234
print(len(s))
# wrong
'''


#--------------------------------------- remember
# // is floor division (integer division)

n=456
'''Step	      Operation	          Result
----------------------------------------------
num % 10	  Last digit	        6
num // 10	  Remove last digit	    45
45 % 10    	  Last digit	        5
45 // 10	  Remove last digit	    4
4 % 10	      Last digit	        4
4 // 10	      Remove last digit 	0 (stop)'''