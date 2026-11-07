# Input : mphasisbangalore
# Output: m1p1h1a3s2i1b1n1g1l1r1e1

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

##########################################

def get_half_string(s):
    length = len(s)
    half_length = length // 2
    return s[:half_length]

print(get_half_string("welcometoindia"))


print("Python"[0])


x = [1,2,3]
y = x
y[1] = 4
print(x)

#To keep x unchanged, create a copy:
x = [1,2,3]
#y = x.copy()  # or y = x[:]
y = x[:]
y[1] = 4
print(x)      # [1, 2, 3] — x is unchanged
print(y)      # [1, 4, 3]