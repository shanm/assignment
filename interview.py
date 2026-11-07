# Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a , end=" ")
        a, b = b, a + b
    #return a

fibonacci(10)

print("\n")

#1. Reverse String
def reverse_string(s):
    #print(s[::-1])
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))

# 2. Polindrome Check
def polinrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

polinrome("high")

# 3. Anagram Check
def anagram(s1, s2):
    print(f"Sorted {s1}: {sorted(s1, reverse=True)}")
    print(f"Sorted {s2}: {sorted(s2, reverse=True)}")
    if sorted(s1) == sorted(s2):
        print(f"{s1} and {s2} are anagrams")
    else:
        print(f"{s1} and {s2} are not anagrams")
        
anagram("listen", "silent")

# 4. Factorial
def factorial(n):
    if n < 0:
        return "Facrtorial is not defined for negative numbers"
    result = 1

    for i in range(1, n+1):
        #print(f"i: {i}, result: {result}")
        result *= i

    return result


print(factorial(5))

# Facrorial using recursion
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not define for negative numbers"
    if n ==0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))

import math
print(math.factorial(5))

# 5. Prime Number Check
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

# Find Duplicate in Array
def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

print(find_duplicate([1,3,4,2,2]))

#9. Merge Two Sorted Arrays
def merge_arrays(list1, list2):
    merged = []
    
    
print(merge_arrays([1,3,5], [2,4,6]))

array1 = [1,3,5]
array2 = [2,4,6]

print(sorted(array1 + array2))
print(array1 + array2)
merged = [*array1, *array2]
print(sorted(merged))

#16. Flatten Nested List
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1,[2,[3,4]],5]))

# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Dictionary
person = {"Name": "Mona", "City": "Bangalore"}
#person["Age"] = 5
person.update({"Age" : 5})
print(person)


s1 = {'a': 20}
s2 = {'b': 10}

#{'a': 20, 'b': 10}

merged = {**s1, **s2}
print(merged)


# Set
set = {1, 2, 3, 4}
set.add(5)
set.update([6, 7, 8])
print(set)

# Tuple
point = (2, 3)
point = point + (4,)
print(point)


# Decorators
def logger_func(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
    return wrapper

@logger_func
def add(a, b):
    return a + b

add(5, 10)


# Generators
def squares(n):
    for i in range(n):
        yield i * i
        
for s in squares(5):
    print(s, end=" ")
    
# Normal function to return squares
def square_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

print(square_list(5))


# Wrire Asyn program
import asyncio

async def task1():
    print("Task1 is started")
    await asyncio.sleep(2)
    print("Task1 is completed")
    
async def task2():
    print("Task2 is started")
    await asyncio.sleep(2)
    print("Task2 is completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Asyncio with HTTP request
import aiohttp

async def get_users():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typecode.com/users") as response:
            return await response.json()
        
# Async in FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_users():
    users = await get_users()
    return users

# Context Manager
with open("file.txt", "w") as f:
    f.write("Hello World")

#Custom Context Manager
class FileManager:
    def __init__(self, file_name, mode):
        self.filename = file_name
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        # Setup: Open the resource
        self.file = open(self.filename, self.mode)
        return self.file  # Bound to the 'as' variable
    
    def __exit__(self, exc_type, exc, tb):
        # Teardown: Close the resource
        if self.file:
            self.file.close()

        # Returning False allows exceptions to propagate normally
        return False
    
    
# Mutithreadin
import threading
        

####################

# Wrire Asyn program
import asyncio

async def task1():
    print("Task1 is started")
    await asyncio.sleep(2)
    print("Task1 is completed")
    
async def task2():
    print("Task2 is started")
    await asyncio.sleep(2)
    print("Task2 is completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Asyncio with HTTP request
import aiohttp

async def get_users():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typecode.com/users") as response:
            return await response.json()
        
# Async in FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_users():
    users = await get_users()
    return users

# Context Manager
with open("file.txt", "w") as f:
    f.write("Hello World")

#Custom Context Manager
class FileManager:
    def __init__(self, file_name, mode):
        self.filename = file_name
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        # Setup: Open the resource
        self.file = open(self.filename, self.mode)
        return self.file  # Bound to the 'as' variable
    
    def __exit__(self, exc_type, exc, tb):
        # Teardown: Close the resource
        if self.file:
            self.file.close()

        # Returning False allows exceptions to propagate normally
        return False
    
    
# Mutithreadin
import threading
        

#############################
#what is the output of this code
a = [1, 2, 3, 4, 5, 6]
for i in range(len(a) - 1, -1, -2):
   print(i)
   a[i] = 0
print(a)

#output: [0, 2, 0, 4, 0, 6]
##################
#Write a function which finds the sum of all odd digits and the sum of all even digits from a list of numbers.
nums = [123, 456, 789, 10]
def sum_odd_even_digits(nums):
    odd_sum = 0
    even_sum = 0

    for num in nums:
        for digit in str(num):
            digit = int(digit)

            if digit % 2 == 0:
                even_sum += digit
            else:
                odd_sum += digit

    return odd_sum, even_sum


nums = [123, 456, 789, 10]

odd_sum, even_sum = sum_odd_even_digits(nums)

print("Sum of odd digits:", odd_sum)
print("Sum of even digits:", even_sum)