# Write a recursive program to:
#     Convert a decimal number to binary
#     Print the binary digits in correct order


# ex:-13
'''divide by 2 '''


# Recursive program to convert decimal to binary

def dec_to_bin(num):
    if num == 0:
        return
    dec_to_bin(num // 2)
    print(num % 2, end="")

num = int(input("Enter a decimal number: "))
print("Binary equivalent:", end=" ")
dec_to_bin(num)



# Decimal to Binary without recursion

def dec_to_bin():
    num = int(input("Enter a decimal number: "))

    if num == 0:
        print("Binary: 0")
        return

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    print("Binary:", binary)

dec_to_bin()





# ----------------------------- correct ans but wrong way

# def dec_to_bin():
#     num=int(input("enter the number to be converted "))

#     rem_list=[]
#     while(num>0):
#         rem=num%2
#         num=num//2
#         rem_list.append(rem)
#     rem_list.reverse()
#     print(rem_list)
    
#     # print(quitiont)

# dec_to_bin()


'''
# -------------- exrtacting one one number from sumber
num=143
sum=0
while(num>0):
    rem=num%10
    num=num//10
    sum=sum+rem

print(sum)'''