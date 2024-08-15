# -----------------------------else in for loop

# eg1
for i in range(5):
    print(i)
else:
    print("sorry no i")

print("\n")

# eg2 --> working with empty list
for i in []:
    print(i)
else:
    print("sorry no i")

# eg3 --> interviiew question (pridect output)
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry no i")

print("\n")
# eg 4 (same with wile loop)
i=0
while(i<7):
    print(i)
    i=i+1
    if i == 4:
        break
else:
    print("sorry no i")