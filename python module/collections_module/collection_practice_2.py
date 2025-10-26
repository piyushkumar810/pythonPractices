# Using a loop, collect 10 shopping items as input. Use a Counter to count 
# occurrences and display the most common item. If there’s a tie, display all tied items.

from collections import Counter

# ---------------------- this will return all items which occured more than 2,but i have to find most occuring item
# counter=0
# item_list=[]
# for i in range(6):
#     counter+=1
#     item_list.append(input(f"enter {counter} items : "))
# print(item_list)

# list2=Counter(item_list)
# print(list2)
# for item,freq in list2.items():
#     if freq>=2:
#         print(f"most common items are:  {item} which occured {freq} times")



# ------------------ correct code
from collections import Counter

# Collect 10 shopping items as input
items = []
for i in range(10):
    item = input(f"Enter item {i + 1}: ").strip().lower()
    items.append(item)

# Count occurrences
counts = Counter(items)
print("\nItem frequencies:", counts)

# Find the highest frequency
max_count = max(counts.values())

# Find all items that have this max frequency
most_common_items = [item for item, freq in counts.items() if freq == max_count]

# Display results
print("\nMost common item(s):")
for item in most_common_items:
    print(f"{item} (occurred {max_count} times)")
