# -------------------------------------1st python interview

# Q1) introduce yourself in brief ?
''' ans--> Good afternoon, sir/ma'am. My name is Piyush Kumar.
        In my family, apart from my parents, I have one elder brother and one elder sister.

        I completed my intermediate education at DAV Public School, Bokaro, and recently graduated 
        from Vinoba Bhave University, Hazaribagh, with an overall CGPA of 7.5.

        During my studies, I acquired(learned) various technical skills, including C, C++, Java, Python, HTML, 
        CSS, Node.js, Express.js, and database technologies like MongoDB and MySQL. These skills enabled
        me to successfully develop my final year project, Car Rental System, a full-stack web 
        application based on the MERN technology stack (excluding React).

        With these skills and project experience, I secured a position at Bulwark Software Private
        Limited. While working on projects, I also discovered and honed additional skills such as
        problem-solving, time management, teamwork, and adaptability.'''

# Q2) you have any achievements in your carrier ?
'''ans-> My Achievements:
        During my graduation, I achieved a CGPA of 7.5 in my final year. Additionally, 
        I participated in a coding competition organized by AISECT University, where I secured the
        10th rank and received a certificate of recognition. '''

# Q3) how much you rate pyhton out of 5 ? 
'''ans-> 4 '''

# Q4) what do you mean by variable in pyhton ?
'''ans-> variables are like a container which is used to store a values like example :- 
        a=10, a="piyush" , here a is variable which stores 10 and piyush in memory
        
        there are some rules to define a variable:-
        --> a variable can be made up of (alphabets, underscore and numbers)
        --> a variable can start with alphabets and underscore

        Rules:-
        --> no keywords can be used to create a variable
        --> the 1st letter of variable should be small.
        --> variable name should not be seperated with space.
        --> the 1st letter should not start with number or special symbol.
        '''

# Q5) what is the use of decision making statements ?
'''ans-> decision making statements are used to make decisions based to some conditions '''

# Q6) can you differentate all the decisions making statements ?
'''ans-> there are 4 types of decision making statements in pyhton :-
        1st - if statement
                this is a simple decision making statement where only true block participate in the 
                execution , if condition satisfies then it will go for execution otherwise nothing 
                for it.
                
        2nd - if else statement
               in this statement both true and false block will execute / or participate in the execution
               based on condition
               
        3rd - elif statement
              it allow checking multiple conditions if it is true otherwise. The else block executes
              if none of the conditions are true
              
        4th - nested if-else statement
              in this statement , if and else block contains another if-else ststement
              then such type of arrengment is called nested if-else statement
              
        5th - switch (match case in Python 3.10+)
              Matches a value against multiple cases and executes the block corresponding to the matching case'''

# Q7) write a program to find a given number is strong no or not ?
''' ans -> A strong number is a number in which the sum of the factorials of its digits equals the number itself.

            For example, 145 is a strong number because:
            1! + 4! + 5! = 1 + 24 + 120 = 145.'''

# def strong_number(n):
#     sum=0
#     original_no=n

#     while(n!=0):
#         digit=n%10
#         n=n//10

#         factorial=1
#         temp=digit
#         while(temp>=1):
#             factorial=factorial*temp
#             temp -=1

#         sum=sum+factorial
#     if(sum==original_no):
#         return f"yes {original_no} is a strong number"
#     else:
#         return f"no {original_no } is not a strong number"

# n=int(input("enter the number you want to check = "))
# result=strong_number(n)
# print(result)


# Q8) what is the difference between list and tuple ?
'''ans -> 1st-> list are mutable object on the other hand tuple are immutable objects .
          2nd-> list is denoted with square bracket on the other hand tuple is denoted by 
                perenthises ()
          3rd-> performance difference in between we can add elements in the list whereas
                in tuple once created we cannot add the new elements.'''

# Q9) what do you mean by list comprehension ?
'''ans -> List comprehension is a concise and elegant/simple way to create lists in Python'''

# Q10)please create a list with 1-10 even numbers using list comprehension?
list=[x for x in range(1,11) if x % 2==0]
print(list)

# Q11) tell me about string ?
'''ans-> string is a sequence of characters which is enclosed with single quote or double quote
         .its an mutable object in python'''

# Q12) write a program to check given string is palindrome or not ?
'''ans-> A palindrome is a word, number, phrase, or sequence of characters that reads the
         same backward as forward, eg:-Words: "madam", "racecar", 121, 1331 etc... '''

def palindrome(str):
    original_str=str
    reversed_str=""
    
    # using shortcut for reversing the string
    # str1=str[ ::-1]
    # print(str1)

    n=len(str)
    for i in range(n-1,-1,-1):
        reversed_str += str[i]
    print(reversed_str)

    if original_str == reversed_str:
        print(f"Yes, '{original_str}' is a palindrome.")
    else:
        print(f"No, '{original_str}' is not a palindrome.")

str=input("Enter the string you want to check = ")
result=palindrome(str)

# Q13) what do you mean by generator in python ?
'''ans-> generator is an object in pyhton which is used to create value one at a time
         insted of all at once
         
         it uses "yield" keyword to return the value'''

# Q14) what do you mean by closure ?
'''ans-> a closure is a function that returns a variable enclosing in its lexical scope'''

# Q15) when do we need to use closure ? 
'''ans -> ones function is creater after the execution the memory will we distroyed but, 
          you want that variable to be used outside the function there we use closure'''

# Q16) what is the difference between procedural oriented programming and object oriented programming ?
'''ans-> POP: Focuses on functions or procedures as the primary way to operate on data.
         OOP: Focuses on objects that encapsulate both data and behavior.
         
         POP: Data is typically shared globally and can be modified by any function.
         OOP: Data is encapsulated within objects, and access is restricted through methods 
               (functions within objects).
               
        POP: it follows top-down approach
        OOP: it follows bottom-up approach'''

# Q17) what do you mean by top-down approach and bottom-up approach ?
'''ans-> Top-Down Approach:

         Start with the big picture or the main problem.
         Break it into smaller parts (sub-problems).
         Solve each part step by step.
         
        Bottom-Up Approach:

        Start with the smallest pieces or basic tasks.
        Combine them step by step to build the solution.'''

# Q18) what is inheritance in python?
'''ans->  inheritance allows a class (child class) to inherit methods and properties
          from another class (parent class). This helps in reusing code and 
          extending functionality.'''


# Q19) what is mro ?
'''ans -> The MRO determines the order in which methods are looked up in the class
          hierarchy when calling a method or accessing a property.'''