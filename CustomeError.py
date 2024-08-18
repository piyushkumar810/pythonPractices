# -------------------------------------raising custom error in pyhton

a=int(input("Enter a value between 5 and 9 : "))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")

# eg 2

n=input("Enetr any string you want : ")
if(n !="quit"):
    raise SystemExit("quit not found")