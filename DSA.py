def merge_intervals(intervals):
    if not intervals:
        return []
    
    # sort by the start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
          merged.append(current)  
    return merged

intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals(intervals))

########################################

# 1. Ratate array right by k () in-place
# Problem: Given an array and integer k, rotate the array to the right by k steps 
# in-place
def rotate(nums, k):
    n = len(nums)
    k %= n
    def rev(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1; j-=1
    rev(0, n-1)
    rev(0, k-1)
    rev(k, n-1)

#Example
arr = [1,2,3,4,5,6,7]
rotate(arr, 3)
print(arr) #[5,6,7,1,2,3,4]

"""
Explanation:
    Revers whole array, reverse  first k, reverse rest..
    Complexity: O(n) time, O(1) extra space
    Tip: Handles large k with k %= n.
"""

# 2. Merge Overlapping intervals.
"""
Given intervals [[s,e], ...], merge overlapping intervals
Example: [[1,3], [2,6], [8,10], [15,18]] -> [[1,6], [8,10], [15, 18]]

"""

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for s,e in intervals[1:]:
        last_s, last_e = merged[-1]
        if s <= last_e:
            merged[-1][1] = max(last_e, e)
        else:
            merged.append([s,e])

    return merged

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
# [[1,6], [8,10], [15, 18]]

"""
Explanation: Sort by start; iterate merging when overlap.
Complexity: O(n log n) due to sort
"""

# Majority Element
def majority_elements(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(majority_elements([3,2,3]))
print(majority_elements([2,2,1,1,1,2,2]))

# Longest common prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = list(strs[0])
    for s in strs[1:]:
        i=0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:1]
        if not prefix:
            return ""
    return "".join(prefix)

print(longest_common_prefix(["flower", "flow", "flight"])) # result - "fl"

# Two Sum
# Problem given nums and target, return indices of the two numbers adding to target
# Example: nums = [2,7, 11, 15], target =9 -> [0,1]
# Approach Hashmap of value -> index while iterating. A window function performs calculation
# accross a set of table rows related to the current row- without collapsing rows like GROUP BY

def two_sums(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        want = target-x
        if want in seen:
            return [seen[want], i]
        seen[x]=i
    return []

print(two_sums([2,7,11,15], 9)) # [0,1]
# Complexity: O9n) time, O(n) space 