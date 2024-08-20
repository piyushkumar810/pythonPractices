# -----------------------------------------KBC (kaun banega crorepati)---------------------------------------------
print("--------------------------------------------------🫸🫷  WELCOME TO KBC  🫸🫷---------------------------------------------")
print("\n")

questions=[
    ["What is a computer?", "A machine that can store and process data",
      "A device for listening to music", "A kitchen appliance", "A tool for gardening",
     1],

    ["What are the main components of a computer?",
      "Monitor, keyboard, and mouse", "CPU, memory, and storage",
        "Printer, scanner, and speakers", "None of the above", 
     2],

    ["What is the difference between hardware and software?", 
     "Hardware is the physical parts of a computer, software is the programs",
       "Hardware is the programs, software is the physical parts", 
       "Hardware is the power supply, software is the storage", "None of the above",
     1],

    ["What is an operating system?", "A type of hardware",
      "Software that manages computer hardware and software resources", 
      "A peripheral device", "An application software", 
     2],

    ["What are the different types of operating systems?", 
     "Windows, MacOS, Linux", "Microsoft Word, Excel, PowerPoint",
       "Google, Bing, Yahoo", "None of the above", 
     1],

    ["What is the function of the CPU (Central Processing Unit)?", 
     "To store data", "To process instructions and manage the operation of the computer",
       "To display images on the screen", "To provide power to the computer",
     2],

    ["What is RAM (Random Access Memory) and why is it important?", 
     "It stores data permanently", 
     "It temporarily holds data and instructions that the CPU needs", 
     "It connects different parts of the computer", "It cools down the computer", 
     2],

    ["What is the difference between RAM and ROM (Read-Only Memory)?", 
     "RAM is permanent storage, ROM is temporary storage", 
     "RAM is temporary storage, ROM is permanent storage", 
     "RAM is used for input, ROM is used for output", "None of the above",
     2],

    ["What are input and output devices? Give examples.", 
     "Input devices: Printer, Output devices: Keyboard",
       "Input devices: Keyboard, Output devices: Monitor", 
       "Input devices: Monitor, Output devices: Scanner", 
       "Input devices: Speaker, Output devices: Mouse", 
     2],

    ["What is the function of a motherboard?", "To power the computer", 
     "To connect and allow communication between various components of the computer",
       "To display images", "To store data", 
     2],

    ["What is the purpose of a hard drive?", "To process data", 
     "To temporarily store data", "To permanently store data", "To connect peripherals",
     3],

    ["What is a network, and what are the different types of networks?", 
     "A system that converts data, Types: Digital and Analog", 
     "A group of computers connected together, Types: LAN, WAN, MAN", 
     "A type of software, Types: Application and System", "None of the above", 
     2],

    ["What is the Internet, and how does it work?", 
     "A local network that connects computers within a building", 
     "A global network that connects millions of private, public, academic, business, and government networks", 
     "A software application", "A type of hardware", 
     2],

    ["What is cloud computing?", 
     "Storing and accessing data and programs over the internet instead of on a local computer", 
     "A type of input device", "A software development process", 
     "A computer programming language", 
     1],

    ["What is an IP address and why is it important?", 
     "It is a type of software, important for running applications", 
     "It is a unique address that identifies a device on the Internet or a local network, essential for communication", 
     "It is a hardware component", "None of the above", 
     2],

    ["What are the differences between a compiler and an interpreter?", 
     "A compiler translates code into machine language all at once, an interpreter translates code line by line", 
     "A compiler is a type of hardware, an interpreter is a type of software",
     "A compiler is used for high-level programming, an interpreter is used for low-level programming", 
     "None of the above", 
     1],

    ["What is cybersecurity, and why is it important?", 
     "The practice of protecting computers and networks from theft, damage, and unauthorized access", 
     "A type of computer programming", "A type of hardware", "None of the above", 
     1]
]

# taking price money in a list
prize_money_list = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹1,00,00,000 (1 Crore)",
    "₹5,00,00,000 (5 Crore)",
    "₹7,00,00,000 (7 Crore)"
]

money=0
for i in range(0,len(questions)):
    question=questions[i]
    print("Question for ",prize_money_list[i])
    print("Q.",(i+1), question[0])
    print("-------------------------------------------------------------Options---------------------------------------------------")
    print("A ",question[1],"                                  ","B ",question[2])
    print("C ",question[3],"                                  ","D ",question[4])


    reply=int(input("Enter your answer (1-4) "))
    if(reply==question[5]):
        print("Correct answer you have won ", prize_money_list[i])
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
        elif(i==17):
            money=70000000
    else:
        print("sorry wrong Answer 😩😩😩😩😩")
        print("finally you won ",money ,"🤑🤑🤑🤑🤑")
        break
    print("\n")


