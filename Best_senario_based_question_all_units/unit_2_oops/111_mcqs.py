'''
Q7. Identify the error:
def set_price(self, price):
    self.__price = self.__price + price

A. Syntax error
B. Setter name is wrong
C. Setter logic is incorrect
D. Getter missing

✅ Answer: C
🧠 Explanation:
A setter should set, not increment, unless explicitly intended.


Q10. Why should validation be added in setter methods?

A. To reduce code length
B. To improve readability
C. To prevent invalid object state
D. To allow inheritance

✅ Answer: C
🧠 Explanation:
Validation prevents illegal or inconsistent data values.


Q11. Which of the following violates encapsulation?

A. Using getter inside display
B. Using setter with validation
C. Accessing __balance directly
D. Declaring variable as private

✅ Answer: C
🧠 Explanation:
Direct access to private variables breaks encapsulation.
'''

# -------------- note
# 🧠 EXAM MEMORY KEYS

# Getter → read
# Setter → write + validate
# Private variable → __
# Encapsulation → control access, not hide completely