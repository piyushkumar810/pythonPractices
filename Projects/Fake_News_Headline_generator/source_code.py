# importing random module to generate random occurance
import random 

# creating lists
subjects=[
    "Nerander modi",
    "tannmay",
    "virat kohli",
    "rahul gandhi",
    "shraveni",
    "a group of monkeys",
    "a mumbai cat",
    "piyush kumar",
    "auto rickshaw form delhi",
    "arjun verma",
    "a flock of pigeons",
    "a bengaluru dog",
    "megha patil",
    "parneet kumar",
    "a red bus from kolkata",
    "neha sharma",
    "a herd of elephants",
    "a chai vendor from mumbai",
    "rohan mehta",
    "nekhil kumar",
    "a group of dancers",
    "a pune street artist",
    "giya",
    "a delhi metro train",
    "sneha singh",
    "a pack of wolves"
]
# print(len(subject))

actions=[
    "dances with",
    "declear War with",
    "eats",
    "goes temple",
    "borrows slippers from",
    "argues with",
    "throws banana at",
    "sings lullaby to",
    "steals lunch from",
    "gives marriage advice to",
    "plays chess with",
    "tickles",
    "writes poetry about",
    "forgets birthday of",
    "dances awkwardly with",
    "shares pani puri with",
    "runs marathon against",
    "takes selfie with",
    "borrows money from",
    "competes in staring contest with",
    "accidentally hugs",
    "does karaoke with",
    "blames traffic on"
]
# print(len(actions))

place_or_things = [
    "a haunted library",
    "the Delhi metro",
    "a flying scooter",
    "a Mumbai beach",
    "a broken TV remote",
    "the Eiffel Tower of Noida",
    "a magic refrigerator",
    "a lost umbrella",
    "the Bengaluru traffic signal",
    "a floating teacup",
    "a talking ATM machine",
    "the Chennai railway station",
    "a golden rickshaw",
    "a confused robot",
    "the secret canteen of Hogwarts",
    "a dancing coconut tree",
    "a sleeping laptop",
    "the haunted hostel room",
    "a talking parrot statue",
    "a leaking water bottle",
    "a flying dosa stall",
    "the invisible classroom",
    "a spicy samosa factory"
]
# print(len(place_or_things))

while True:

    print("------------- Welcome To Our News Nation \" हँसते हँसते पढ़ो \" --------------- ")

    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(place_or_things)

    Headline=f"BREAKING NEWS : 🤣🤣 {subject} {action} {place_or_thing}  🤣🤣"
    print("\n", Headline)
    
    user_input=input(" \n Do You Want To Read More HeadLine (yes/no)").strip().lower()

    if(user_input == "no"):
        break

print("----------------- Thank You So Much, When you get borred you must read again ----------------")