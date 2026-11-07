def twoSum(nums, target):
    seen = {} # value -> index
    matched = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            matched.append((seen[complement], i))
        seen[num] = i
    return matched

nums = [5,7,2,3,4,5]
print(twoSum(nums, 9))

###################################
def find_pairs(arr, target):
    seen = set()
    result = []
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((complement, num)))
            if pair not in result:
              result = []
              result.append(pair)
        seen.add(num)
    return result


a = [5, 7, 2, 3, 4, 5]
target = 9

print(find_pairs(a, target))

#######################################
# Problem:   Given a list of transactions with (amount, type) where type is "credit" or "debit", calculate the final account balance.
 
# transactions = [(1000, "credit"), (500, "debit"), (200, "credit")]


# print(calculate_balance(transactions))  # Output: 700

# def calculate_balance(transactions):
#     balance = 0
#     for amount, ptype in transactions:
#         if ptype == 'credit':
#           balance +=  amount
#         elif ptype == 'debit':
#             balance -=  amount
#     return balance
    

# transactions = [(1000, "credit"), (500, "debit"), (200, "credit")]

# print(calculate_balance(transactions))

# Given a list of employees with their working hours per week, calculate the total overtime pay.
# Overtime is defined as hours worked beyond 40 per week.
# Overtime rate = 1.5 × hourly wage.
# employees = [
#     ("Alice", 45, 100),   # name, hours, hourly_wage
#     ("Bob", 38, 80),
#     ("Charlie", 50, 120)
# ]
#print(calculate_overtime(employees))
# Output: {'Alice': 750.0, 'Bob': 0, 'Charlie': 1800.0}

def calculate_overtime(employees):
    emp_wage = {}
    avg_hrs = 40
    hourly_wage = 1.5
    for item in range(len(employees)):
        #print(employees[item][0])
        if employees[item][1] < avg_hrs:
           emp_wage[employees[item][0]] =  0
        else:
           print(employees[item][1] - avg_hrs)
           emp_wage[employees[item][0]] =  hourly_wage * employees[item][2]  * (employees[item][1] - avg_hrs)
           
    return emp_wage

employees = [
    ("Alice", 45, 100),   # name, hours, hourly_wage
    ("Bob", 38, 80),
    ("Charlie", 50, 120)
]
print(calculate_overtime(employees))

#########################################################

def find_pairs(arr, target):
    seen = set()
    result = []
    for num in arr:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((complement, num)))
            result.append(pair)
        seen.add(num)

    return result

a = [5, 7, 2, 3, 4, 5]
target = 9

print(find_pairs(a, target))

######################################
# Input: nums = [2,7,11,15], 
# target = 9

# Output: [0,1]

# Explanation: 
# Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                result.extend([i, j])
    return result


nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))

##################
def groupAnagram(strs):
    groups = {}
    result = {}

    for st in strs:
        key = "".join(sorted(st))
        groups.setdefault(key, []).append(st)

    for group in groups.values():
        first = group[0]
        result[first] = group[1:]

    return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))

###################################

from collections import defaultdict
def groupAnagram(strs):
  groups = defaultdict(list)
  
  for word in strs:
      key = "".join(sorted(word))
      groups[key].append(word)
  
  return { group[0]: group[1:]  for group in groups.values()}

strs = ["eat","tea","tan","ate","nat", "bat", "abt"]
print(groupAnagram(strs))

########################
#First Missing Positive
# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
def firstMissingPositive(nums):
    n = len(nums)
    i = 0

    while i < n:
        correct = nums[i] - 1

        if 1 <= nums[i] <= n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

########################
def reverse_negative_string(num):
    if num < 0:
        return -int(str(abs(num))[::-1])
    return int(str(num)[::-1])

print(reverse_negative_string(-12345))

 