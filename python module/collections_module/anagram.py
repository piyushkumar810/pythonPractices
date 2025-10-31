# Read N words; use defaultdict(list) to group anagrams. Print only groups with size ≥ 3.

'''
what is anagram?
--> Anagrams are words made up of the same letters in a different order.
eg:- input=
    eat
    tea
    tan
    ate
    nat
    bat
    tab
    ant

output:- 
"eat", "tea", "ate"  → all are anagrams
"bat", "tab"         → anagrams

'''
from collections import defaultdict

# Step 1: Read how many words to input
N = int(input("Enter number of words: "))

# Step 2: Read N words (simple version)
words = []
for i in range(N):
    word = input("Enter word: ").strip()
    words.append(word)

# Step 3: Create a defaultdict to store anagram groups
anagrams = defaultdict(list)

# Step 4: Group words by their sorted character key
for word in words:
    key = ''.join(sorted(word))   # sorting letters of each word
    anagrams[key].append(word)

# Step 5: Print only groups with size >= 3
print("\nGroups with 3 or more anagrams:")
for group in anagrams.values():
    if len(group) >= 3:
        print(group)
