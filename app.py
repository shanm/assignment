s = "python is great language"
print(len(s.split()))

chars = "My Name Is eeeeeeee Shanmuga"
#print(max(chars.split()))
max_length = len(max(chars.split()))
print(max_length)
max_words = [word for word in chars.split() if len(word) == max_length]
print(max_words)

##################

s = "programming"
unique = "".join(dict.fromkeys(s))
print(unique)

a =[1,2,3]
b= [3,4,5]
print(list(set(a) | set(b)))

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
print(list(set(d1) | set(d2)))
common = list(set(d1) & set(d2))
print(common)

for i in range(1, 6):
    print("* " * i)
    
# Nested comprehension
matrix = [[ i * j for j in range(1,4) ] for i in range(1,4)]
#print(matrix)
for row in matrix:
    print(row)
    
# List : stores all the values in memory
square_list = [x**2 for x in range(100000)]

# Generator: computes on demand
square_gen = (x**2 for x in range(100000))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

###################################
s = "mphasisbangalore"

freq = {}

# Count occurrences
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
# Build output preserving first occurrence order
result = ""
seen = set()

for ch in s:
    if ch not in seen:
        result += ch + str(freq[ch])
        seen.add(ch)

print(result)

res = ""
for key, value in freq.items():
    res += str(key) + str(value)
    
print(res)

x=5
x += 3
print(x)

x=b"ABC"
print(x[0])

###########################################

num = [1,2,3,4,5,6,7,8,3,3,3,4,4,4,5,5,5,1,1]

duplicate = []
for n in num:
    print(num.count(n))
    if n not in duplicate and num.count(n) >= 2:
       duplicate.append(n) 
       
print(duplicate)

###################
# Star Pattern

target = 5
for i in range(1, target+1):
    print(" "*(target-i) + "* "*i)
    
#####################################
l = [1,2,3,4,5,6]

result = [(i**2 if i%2 == 0 else i) for i in l]
print(result)

#############################

def flattern(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flattern(item))
        else:
            result.append(item)
    return result

l = [1,[2,3],[4],5,[6,7]]
print(flattern(l))

##############################
d = [
{'name': 'David', 'age': 32},
{'name': 'Tom', 'age': 24},
{'name': 'John', 'age': 26}
]

sorted_dict = sorted(d, key=lambda d: d["age"], reverse=True)
print(sorted_dict)

#################################

def remove_sp(func):
    print(func.__name__)
    def wrapper(name):
        cleaned_name = (f for f in name if f.isalnum())
        #print("Generator => ", cleaned_name)
        print("Helo => ", ''.join(cleaned_name))
        return ''.join(cleaned_name)
    return wrapper

@remove_sp    
def test(name):
    return name

print(test('A@mantya!'))


import re

text = "A@mantya!"
print(re.sub(r'[^a-zA-Z0-9]', '', text))

###############################

def is_prime(num):
    if num <= 1:
        return False
    #print(int(num ** 0.5) + 1)
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False

    return True
    
print(is_prime(127))

##################################
#Better Solution (O(n))
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

list1 = [1, 2, 3, 4, 5, 1, 2, 3, 3, 3, 3]
print(find_duplicates(list1))

###################################
nums = [1,2,3,4,5,6,7,8,9]
target = 13

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)

##################################
nums = [1,2,3,4,5,6,7,8,9]
target = 13

result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result.append((i, j))

print(result)

############################
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
