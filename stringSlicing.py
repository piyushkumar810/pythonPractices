# -----------------------------how to get length of string
name='guido van rassum'
leng1=len(name)
print('python developer has', leng1,"character")

# -------------------------------slicing operation in python
print(leng1)
print(name[0:5])

print(name[0:9])
print(name[:9])
# python bydefault considered starting index with 0 if that index is blank

print(name[3:])
# python bydefault considered last index with (length of string) if that index is blank

print(name[:])
# is means starting from 0 and ending with length of string

print("\n negative indexing \n")

print(name[0:-3])
# means starting fron 0 and ending with (len(name)-3 => 16-3 = 13)

print(name[-3:-1])