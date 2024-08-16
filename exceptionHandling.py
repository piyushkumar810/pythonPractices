# -----------------------------------Exception Handling in pyhton

a=input("Enter a value : ")
print(f"Multiplication table of {a} is ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("some important lines of code")
print("end of program")