'''
Q2. In OOP, the term “oriented” refers to:

A. Data flow direction
B. Function execution order
C. Direction toward modeling real-world objects
D. Syntax direction

✅ Correct Answer: C

🧠 Explanation:
Object-oriented programming is directed toward modeling objects, not procedures or execution steps
.'''


'''
Q4. When a class is written, what does it primarily define?

A. Unique values for each object
B. Memory allocation for objects
C. General behavior of a category of objects
D. Execution sequence

✅ Correct Answer: C

🧠 Explanation:
A class defines general behavior and structure; unique values are assigned when objects are created.
'''


'''
Q5. Objects created from the same class:

A. Have different methods
B. Share common characteristics but have unique values
C. Are completely independent in behavior
D. Cannot access class methods

✅ Correct Answer: B

🧠 Explanation:
Objects share methods and structure from the class but can have different attribute values.
'''

'''
Q9. The main aim of Object-Oriented Programming is to:

A. Speed up program execution
B. Bind data and functions together
C. Reduce memory usage
D. Eliminate errors

✅ Correct Answer: B

🧠 Explanation:
OOP aims to bind data and the functions operating on it, preventing unauthorized access.
'''


'''
Q13. Which OOP feature improves code maintenance by isolating changes?

A. Inheritance
B. Encapsulation
C. Polymorphism
D. Modularity

✅ Correct Answer: D

🧠 Explanation:
Modularity allows objects to be self-contained, so changes in one object don’t affect others.
'''


'''
Q17. Which OOP concept allows objects to send and receive messages?

A. Modularity
B. Encapsulation
C. Object interaction
D. Polymorphism

✅ Correct Answer: C

🧠 Explanation:
Objects interact by sending messages (method calls) to each other.
'''

'''
Q20. Which feature makes OOP flexible and adaptable?

A. Inheritance
B. Encapsulation
C. Polymorphism
D. Modularity

✅ Correct Answer: C

🧠 Explanation:
Polymorphism allows the same interface to behave differently, making systems flexible.
'''

'''
🔥 Exam Strategy
MCQs love definitions + advantages
If question says:
Security / binding → Encapsulation
Reuse / duplication → Inheritance
Flexibility → Polymorphism
Maintenance → Modularity'''


'''
9️⃣ Object Creation (Instantiation)
laptop1 = Laptop("Dell", "Inspiron 15", 55000)
laptop2 = Laptop("Apple", "MacBook Air", 120000)

What Happens Internally?
Python creates a new object
Calls __init__() automatically
Passes:
self → object reference
brand, model, price → user values

📌 This process is called Instantiation
'''


'''
| Attribute                      | Method               |
| ------------------------------ | -------------------- |
| Stores data                    | Performs action      |
| Variable                       | Function             |
| Defined using `self.variable`  | Defined using `def`  |
| Represents state               | Represents behavior  |
| No parentheses while accessing | Parentheses required |
'''

'''
Q3 (Code – Missing Parentheses)
class Demo:
    def show(self):
        return "Hello"

obj = Demo()
print(obj.show)


A. Hello
B. Error
C. <bound method>
D. None

✅ Answer: C

🧠 Explanation:
Without (), Python prints method reference, not result.
'''

'''
Q5 (Code – Attribute Creation)
class A:
    def set(self):
        self.y = 5

obj = A()
obj.set()
print(obj.y)


A. Error
B. None
C. 5
D. Undefined

✅ Answer: C

🧠 Explanation:
Attributes can be created dynamically inside methods.'''

