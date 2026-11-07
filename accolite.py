# EY
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"},
]

seen = set()
result = []

for d in data:
    #print(tuple(sorted(d.items())))
    key = tuple(sorted(d.items()))
    if key not in seen:
        seen.add(key)
        result.append(d)
        
#print(seen)
print(result)
    
    
############################################

#Virtusa
# Ind vs Sa
# Ind vs Pak
# Ind vs Sl
# Ind vs Aus
# Sa vs Pak
# Sa vs Sl
# Sa vs Aus
# Pak vs Sl
# Pak vs Aus
# Sl vs Aus
def flatten_dict(country):
    sorted_country = []

    for i in range(len(country)):
        for j in range(i + 1, len(country)):
            sorted_country.append(f"{country[i]} vs {country[j]}")

    return sorted_country


country = ["Ind", "Sa", "Pak", "Sl", "Aus"]

print(flatten_dict(country))

##################################

import copy

a = [1, [2, 3]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[1][0] = 99

print(b)
print(c)

#b = [1, [99,l3]]

#c=[1,[2,3]]

###############################################

def test(a=[]):
   a.append(1)
   return a

print(test())
print(test())
print(test())

#[1], [1,1], [1,1,1]

############################################

#RAG
 
#Write a Python function to flatten a nested list.
 
# Input:
# [1, [2, [3, 4]], 5]
# Expected Output:
# [1, 2, 3, 4, 5]
 
# Input:
# [1, [2, [3, [4,5]]], 6, [7,8,[9]]]
# Expected Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
#Write a Python function to flatten a nested list.

def flatten(nums):
    output = []
    for num in nums:
        if isinstance(num, list):
            output.extend(flatten(num))
        else:
            output.append(num)
    return output
 
nums = [1, [2, [3, [4,5]]], 6, [7,8,[9]]]
#nums = [1, [2, [3, 4]], 5]

print(flatten(nums))

####################################
# PRINT OUTPUT
s = 'python'
s = s.replace('p', 'P')
print(s)
s = s.replace('n', 'N')
print(s)
s = s[::-2]
print(s)
s = s.lower()
print(s)
s = s + "!"
print(s)
#############
x = [1,2,3,4]
y = x
y.append(5)
x[0] = 10
y.pop()
print(x,y)
 