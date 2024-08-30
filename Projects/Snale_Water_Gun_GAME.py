# ------------------------------------------snake water gun game
# 1. snake, water and gun game is a variation of children's game like "rock, paper and scissore" where player
#    use their hand gestures to represent a stone, paper or scessire, in this game the gun beats the skane
#   ,the water beats the gun,  and the snake beats the water.

# 2.  write a python program to create a snake water and gun game using proper function.

import random
def game(bot, user):
    if(bot == user):
        return 0
    
    elif(bot == 0 and user == 1):
        return -1
    
    elif(bot == 1 and user == 2):
        return -1
    
    elif(bot == 2 and user == 0):
        return -1
    
    return 1

bot=random.randint(0,2)
user=int(input("Enter 0 for snake, 1 for water and 2 for gun : "))
print(f"your choice is : {user}")
print(f'bot choice is : {bot}')

score=game(bot, user)
if(score == 0):
    print('it is draw')
elif(score == -1):
    print("you Lose")
else:
    print('you Won')