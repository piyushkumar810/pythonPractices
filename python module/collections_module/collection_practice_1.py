# Write a Python program that uses a loop to count the frequency 
# of each character in a given string using collections. 
# Display only those characters whose frequency is greater than 2.

# note:- frequency means same occurence many times. and this is done by couter in collections

from collections import Counter

def count_greater_than_2_character(s):
    frequency = Counter(s)
    print("Character frequencies:", frequency)

    result = []  # list to store characters with frequency > 2
    for char, count in frequency.items():
        if count > 2:
            result.append(f"'{char}': {count}")
    # print(result)
    '''
    output:-
    ["'s': 3", "'h': 3", "' ': 4"]
    '''
    return result


user_input = input("Enter the string: ")
result = count_greater_than_2_character(user_input)

if result:
    print("\nCharacters with frequency greater than 2:")
    for r in result:
        print(r)
else:
    print("\nNo character in the string occurs more than 2 times.")


# note :- freq.items()--> This returns a list of (key, value) pairs from the Counter (or dictionary).
''''
for char, count in freq.items():

This is a loop that unpacks each key–value pair:
        char → the character (the key)
        count → how many times it appears (the value)
'''