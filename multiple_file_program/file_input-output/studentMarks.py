# -------------------------------managing the record
# hum three subject ke three student ke marks saved hai studentMarks.txt file mai

# ab mujhi eise accha se likhna hai
f=open('multiple_file_program/file_input-output/studentMarks.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    print(line)
    # print(f)
    if not line:
        break

    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])

    print(f"marks of student {i} in maths is : {m1}")
    print(f"marks of student {i} in ds is : {m2}")
    print(f"marks of student {i} in pyhton is : {m3}")