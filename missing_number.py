# Solution 1: Using Sum Formula (Optimal)
def find_missing(nums):
    n = max(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [1, 2, 5, 3, 6]
print(find_missing(nums))

#################
# Solution 1: Using Sum Formula (Optimal)
def find_missing(nums):
   n = max(nums)
   expected_sum = n * (n + 1) // 2 
   actual_sum = sum(nums)
   return f"Missing nuber is - {expected_sum - actual_sum}"

nums = [1, 2, 5, 3, 6]
print(find_missing(nums))

#######################
#Fibonacci using generator
def fibinacci(n):
    a, b = 0,1
    for _ in range(n):
        yield a
        a, b = b, a+b

gen_valu = fibinacci(10)

for fib_value in gen_valu:
    print(fib_value)