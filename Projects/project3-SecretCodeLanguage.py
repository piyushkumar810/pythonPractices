# write a program to translate a message into secret code language. use the rule below to translate normal english into secret cose language

# coding
# if the word contains at least 3 characters, remove the first letter and append it at the end 
#          now append three randam character at the starting and the end 
# else:
#     simply reverse the string

# decoding
# if the word contain less than three characters then reverse it 
# else: 
#     remove three characters from start and end. now remove the last letter and append the last letter and append it to the beginning

# ----------------------------------------solution

# message=input("Enter any message you want to send your friend 📩 : ")
# print(message)

# listMessage=message.split(" ")
# print(listMessage)

# print(listMessage[0])
# print(listMessage[3])

# listMessage1=' '.join(listMessage)
# print(listMessage1)

# for n in listMessage:
#     print(n)

# for i in range(len(listMessage)):
#     print(listMessage[i] + " " +str(i))

import random
import string

message=input("Enter any message you want to send your friend 📩 : ")
listMessage=message.split(" ")

coding=False
if(coding == False):
    newMessage=[]
    for msg in listMessage:
        if(len(msg)>=3):
            prefix=''.join(random.choices(string.ascii_letters, k=3))
            suffix=''.join(random.choices(string.ascii_letters, k=3))

            stnew= prefix + msg[1: ] + msg[0] + suffix
            newMessage.append(stnew)
        # elif(len(msg)==1):
            # random=''.join
        else:
            newMessage.append(msg[::-1])
    print(' '.join(newMessage))

else:
    newMessage=[]
    for msg in listMessage:
        if(len(msg)>=3):

            stnew= msg[3:-3]
            # stnew= msg[3:(len(msg)-3)]

            stnew=stnew[-1]+stnew[:-1]
            newMessage.append(stnew)
        else:
            newMessage.append(msg[::-1])
    print(' '.join(newMessage))