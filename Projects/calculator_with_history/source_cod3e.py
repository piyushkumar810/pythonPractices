# getting the current folder path
import os

path = os.getcwd()
# print("Current Folder Path:", path)

folder_path = "C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\pythonPractices\\Projects\\calculator_with_history"
History_file=os.path.join(folder_path, "history.txt")

# with open(History_file, "w") as file:
#     file.write("Hello, this is my first text file!!!")

# print("File created at:", History_file)


# ------------ this function will show the history
def show_history():
    file=open(History_file,"r")
    # file.write("Hello, this is my first text file!!!")
    lines=file.readlines()
    if (len(lines) == 0):
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(History_file,"w")
    file.close()
    print('History cleared. ')

def save_to_history(equation, result):
    file=open(History_file,"a")
    file.write(equation + "= "+ str(result) + "\n")
    file.close()

def calculate(user_input):
    parts=user_input.split()
    if len(parts) != 3:
        print("invalid input. use format: number operator numberr(eg: 8+8 )")
        return
    
    num1= float(parts[0])
    op=parts[1]
    num2= float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("connot divide by zero")
            return
        result = num1 / num2

    else:
        print("invalid operator. use only + - * /. ")
        return
    
    if int(result) == result:
        result= int(result)
    print("Result:", result)
    save_to_history(user_input, result)


def main():
    print("---------- SIMPLE CALCULATOR type (history, clear or exit)-------------")
    while True:
        user_input=input("Enter calculation (+ - * /) or command (history, clear or exit)")
        if user_input=="exit":
            print("Goodbye")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()