# fetching time module and according to that printing good morning, good afternoon, good evening and good night  

# my code
import time
current_time=time.strftime("%H:%M:%S")
print(current_time)

timestamp=int(time.strftime("%H"))

if(timestamp>=5 and timestamp<12):
    print("Good Morning piyush")
    print("-------------------------------------")
    n=input("what do you want morning breakfast : ")
    print("your", n , "is ready")
    print("\n")
elif(timestamp>=12 and timestamp<17):
    print("Good Afternoon piyush")
    print("-------------------------------------")
    print("what do you want in lunch")
    print("\n")
elif(timestamp>=17 and timestamp<21):
    print("Good Evening piyush")
    print("-------------------------------------")
    print("what do you want in Dinner")
    print("\n")
else:
    print("Good night")
    print("------------------------------------")
    print("go to sleep")




''' -----------------------this is used to know indain time with am and pm
formatted_time = time.strftime("%I:%M:%S %p")
print(formatted_time)'''
