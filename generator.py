nums = [x*x for x in range(5)]
print(nums)

nums = (x*x for x in range(5))
for num in nums:
    print(num)
    
##############################
# List: creates 1,000,000 integers in memory at once
nums = [x*x for x in range(1000000)]

# Generator: creates one integer at a time
nums = (x*x for x in range(1000000))
for num in nums:
    print(num)  # process and discard one at a time

############################
import sys

# List comprehension
list_nums = [x*x for x in range(1000)]
print(f"List size: {sys.getsizeof(list_nums)} bytes")

# Generator expression
gen_nums = (x*x for x in range(1000))
print(f"Generator size: {sys.getsizeof(gen_nums)} bytes")

####################
def counter(limit):
    for i in range(limit):
        yield i

for num in counter(500):
    print(f"Counter: {num} and Memory: {sys.getsizeof(num)} bytes")