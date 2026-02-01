
# Write list comprehensions to:
# Print the first and last letter of every name in a list.
# Print a list of strings in uppercase.
# Print the reverse of each name in a list.

list_comp=["piyush","navyaa","priya","prabhat","sonu"]
result=[name[0]+name[-1] for name in list_comp]
print(result)

uppercase_list=[str.upper() for str in list_comp ]
print(uppercase_list)

reverse_name=[rev_name[::-1] for rev_name in list_comp]
print(reverse_name)