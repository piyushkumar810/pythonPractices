# 🔹 UNIT–4
# Data Ingestion & Multiprocessing (🔥 Toughest)
# Section A – Database & APIs
'''
Q1.Write a Python program to:
Connect to PostgreSQL
Fetch records where salary > average salary
'''
import psycopg2

conn=psycopg2.connect(
    dbname="company",
    user="Postgre",
    password="pes@123",
    host="localhost",
    port="5432"
)

if conn:
    print("connection successful")
else:
    print("connection unsuccessful")

cor=conn.cursor()

query = """
SELECT * FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);
"""
cor.execute(query)

rows=cor.fetchall()

for i in rows:
    print(i)

cor.close()
conn.close()







'''
Q2.Write a program to:
Fetch data from a REST API
Parse JSON
Store selected fields in CSV
'''

'''
Q3.Write a program to:
Read data from Google Sheets
Update a specific cell dynamically
'''


# Section C – Multithreading & Multiprocessing
'''
Q5.Write a program to:
Create 3 threads
Each thread computes factorial of a number
'''
import threading

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is {fact}")


# Creating 3 threads
t1 = threading.Thread(target=factorial, args=(5,))
t2 = threading.Thread(target=factorial, args=(7,))
t3 = threading.Thread(target=factorial, args=(4,))

# Starting threads
t1.start()
t2.start()
t3.start()

# Waiting for threads to complete
t1.join()
t2.join()
t3.join()

print("All threads completed")





'''
Q6.Write a Python program using multiprocessing to:
Find sum of elements of an array in parallel

import threading
print(threading.current_thread().name)
'''