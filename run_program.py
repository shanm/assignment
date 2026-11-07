def append_item(item, items=[]):
    items.append(item)
    return items


print(append_item(1))
print(append_item(2))
print(append_item(3, []))
print(append_item(4))

# How to fix it
def append_item(item, items=None):
    if items is None:
        items = []
        
    items.append(item)
    return items


print(append_item(1))
print(append_item(2))
print(append_item(3, []))
print(append_item(4))

#####################################
a = [1, 2, 3]
b = a
 
a += [4]

print(a)
print(b)

##########################
a = (1, 2, 3)
b = a

a += (4,)
 
print(a)
print(b)

#################################
nums = [1,2,3,4,5,6,7,8,9]
target = 13

seen = {}
matched= []

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        matched.append((seen[complement], i))
    else:
        seen[num] = i

print(matched)

#############################
nums = [1,2,3,4,5,6,7,8,9]
target = 13

seen = set()
matched = []

for num in nums:
    complement = target - num
    if complement in seen:
        matched.append((complement, num))
    
    seen.add(num)

print(matched)

############################
# Write a program that will find the sum of all the prime numbers between 1 and n
def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
    
    
def add(number):
    total = 0
    for n in range(2, number+1):
        if is_prime(n):
            total += n
    return total
    
print(add(10))