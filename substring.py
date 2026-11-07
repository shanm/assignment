def lengthOfLongestSubstring(s:str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

print(lengthOfLongestSubstring("abcbbccd"))

################################################

# Triangular Number - Ascending and Descending Order
def find_peak(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(mid)

        # Check if mid is the peak
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]

        # Still on the ascending side
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1

        # On the descending side
        else:
            right = mid - 1

arr = [1, 3, 7, 15, 25, 40, 60, 45, 20, 10, 2]
print(find_peak(arr))