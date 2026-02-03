# ✅ Async Program with Multiple Tasks (add, sub, mul)
import asyncio

async def add(a, b):
    await asyncio.sleep(1)
    print("Addition:", a + b)

async def sub(a, b):
    await asyncio.sleep(2)
    print("Subtraction:", a - b)

async def mul(a, b):
    await asyncio.sleep(3)
    print("Multiplication:", a * b)

async def main():
    task1 = asyncio.create_task(add(10, 5))
    task2 = asyncio.create_task(sub(10, 5))
    task3 = asyncio.create_task(mul(10, 5))

    await task1
    await task2
    await task3

asyncio.run(main())


# ------------------------------- or using gather()
# ✅ Async Program using asyncio.gather()
import asyncio

async def add(a, b):
    await asyncio.sleep(1)
    print("Addition:", a + b)

async def sub(a, b):
    await asyncio.sleep(2)
    print("Subtraction:", a - b)

async def mul(a, b):
    await asyncio.sleep(3)
    print("Multiplication:", a * b)

async def main():
    await asyncio.gather(
        add(10, 5),
        sub(10, 5),
        mul(10, 5)
    )

asyncio.run(main())




# 1️⃣ Async: square, cube, power
import asyncio

async def square(n):
    await asyncio.sleep(1)
    print("Square:", n*n)

async def cube(n):
    await asyncio.sleep(2)
    print("Cube:", n*n*n)

async def power(n):
    await asyncio.sleep(1)
    print("Power (n^4):", n**4)

async def main():
    await asyncio.gather(
        square(3),
        cube(3),
        power(3)
    )

asyncio.run(main())




# 2️⃣ Async: sum, average, max of a list
import asyncio

nums = [2, 4, 6, 8]

async def total():
    await asyncio.sleep(1)
    print("Sum:", sum(nums))

async def average():
    await asyncio.sleep(2)
    print("Average:", sum(nums)/len(nums))

async def maximum():
    await asyncio.sleep(1)
    print("Max:", max(nums))

async def main():
    await asyncio.gather(total(), average(), maximum())

asyncio.run(main())





# 3️⃣ Async: factorial of three numbers
import asyncio

async def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    await asyncio.sleep(1)
    print(f"Factorial of {n}:", f)

async def main():
    await asyncio.gather(
        factorial(4),
        factorial(5),
        factorial(6)
    )

asyncio.run(main())





# 4️⃣ Async: string operations (upper, reverse, length)
import asyncio

s = "pesuniversity"

async def to_upper():
    await asyncio.sleep(1)
    print("Upper:", s.upper())

async def reverse():
    await asyncio.sleep(2)
    print("Reverse:", s[::-1])

async def length():
    await asyncio.sleep(1)
    print("Length:", len(s))

async def main():
    await asyncio.gather(to_upper(), reverse(), length())

asyncio.run(main())




# 5️⃣ Async: even, odd, count
import asyncio

nums = [1,2,3,4,5,6]

async def evens():
    await asyncio.sleep(1)
    print("Evens:", [x for x in nums if x%2==0])

async def odds():
    await asyncio.sleep(2)
    print("Odds:", [x for x in nums if x%2!=0])

async def count():
    await asyncio.sleep(1)
    print("Count:", len(nums))

async def main():
    await asyncio.gather(evens(), odds(), count())

asyncio.run(main())