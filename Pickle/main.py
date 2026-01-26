# 🧠 PART 2 — CODING (STEP-BY-STEP, SIMPLE)
# ✅ 1️⃣ Pickling & Unpickling a List
import pickle

data = [10, 20, 30]

with open("list.pkl", "wb") as f:
    pickle.dump(data, f)

with open("list.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)


'''📌 wb → write binary
📌 rb → read binary'''



# ✅ 2️⃣ Pickling & Unpickling a Dictionary
import pickle

student = {"name": "Amit", "age": 20, "city": "Bangalore"}

with open("dict.pkl", "wb") as f:
    pickle.dump(student, f)

with open("dict.pkl", "rb") as f:
    loaded_student = pickle.load(f)

print(loaded_student)



# ✅ 3️⃣ Pickling a Custom Object (VERY IMPORTANT)
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Rahul", 22)

with open("person.pkl", "wb") as f:
    pickle.dump(p, f)

with open("person.pkl", "rb") as f:
    loaded_p = pickle.load(f)

print(loaded_p)


'''📌 Class must be defined before unpickling'''



# ✅ 4️⃣ Pickling Multiple Objects
import pickle

with open("multi.pkl", "wb") as f:
    pickle.dump([1, 2, 3], f)
    pickle.dump({"a": 1}, f)
    pickle.dump("Hello", f)

with open("multi.pkl", "rb") as f:
    print(pickle.load(f))
    print(pickle.load(f))
    print(pickle.load(f))


'''📌 Load order = dump order

🧠 MCQ LOCK — MEMORIZE THESE 10 RULES

1️⃣ Pickling = serialization
2️⃣ Unpickling = deserialization
3️⃣ Pickle stores objects as bytes
4️⃣ Only picklable objects can be stored
5️⃣ Lambda functions ❌
6️⃣ Pickle is Python-specific
7️⃣ Pickle is NOT secure for untrusted data
8️⃣ Pickle preserves object structure
9️⃣ Custom objects can be pickled
🔟 Dump & load order must match'''