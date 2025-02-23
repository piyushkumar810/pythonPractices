# ------------------- nested for loop

for i in range(4):
    for j in range(13):
        if (j%4==0):
            break
        print(j)  

# the output will be nothing because 0%4==0 first conidtion is only true

# to correct this
for i in range(4):
    for j in range(1,13):
        if (j%4==0):
            break
        print(j)  
