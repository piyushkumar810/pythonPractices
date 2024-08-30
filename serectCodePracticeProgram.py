# ------------------------------secret code practice program
import string
import random

def code_word(user1, key):
    b=user1.split()
    lst=[]
    for i in b:
        if(len(i)<3):
            a=i[::-1]
            lst.append(a)
        else:
            code=i[1:] + i[0]
            code1=''.join(random.choices(string.ascii_lowercase,k=key)) + code + ''.join(random.choices(string.ascii_lowercase,k=key))
            lst.append(code1)
    a=' '.join(lst)
    return a

def decord_word(user, key):
    b=user.split()
    lst=[]
    for i in b:
        if(len(i)<3):
            code=i[::-1]
            lst.append(code)
        else:
            code2=i[key:-key]
            try:
                code1=code2[-1]+code2[0:-1]
            except IndexError:
                print('your encryption key is greater than your message')
            lst.append(code1)
    a=' '.join(lst)
    return a

key=None

while True:
    u=input('Enter code or decode or quit : ')
    if(u.lower()=="code"):
        user1=input('Enter your message you want to send : ')
        try:
            key=int(input('enter your key as (3 or 4 or 5) : '))
        except Exception as e:
            print(e)
        try:
            print(code_word(user1,key))
        except Exception as e:
             print('please enter only digit for encryption : ')

             
    elif(u.lower()=="decode"):
        user=input('Enetr your message : ')
        try:
            print(decord_word(user, key))
        except ValueError:
            print('Please enter only a digit for the decryption key.')
        except Exception as e:
            print(f"An error occurred: {e}")


    elif(u.lower()=='quit'):
        break
    else:
        print('please enter valid details : ')
        
# ------------------------------hoooo gaya