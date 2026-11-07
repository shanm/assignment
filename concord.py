# Write
# a program, which will find all such numbers between 1000 and 3000 (both
# included) such that each digit of the number is an even number. The numbers
# obtained should be printed in a comma-separated sequence on a single line

# result = []

# for num in range(1000, 3001):
#     num_str = str(num)
#     if num_str.count('0') != 1 and all(int(digit) % 2 == 0 for digit in str(num_str)):
#         result.append(num_str)
        
#         #str_count = str(num)
#         #if str_count.count(str(0)) > 1:
#         #    result.append(str(num))


# print(",".join(result))

# import pandas as pd
# import random

# df = pd.DataFrame({
#     "Date": pd.date_range(start="2026-07-01", periods=10, freq="D"),
#     "Price": [random.randint(100, 500) for _ in range(10)]
#     })

# print(df)

import pandas as pd
import random
import numpy as np

df = pd.DataFrame({
    "Date": pd.date_range(start="2026-07-01", periods=10, freq="D"),
    "Salary": [random.randint(500, 1000) for _ in range(10)],
    "Age": np.linspace(20, 60, 10).astype(int)
})

print(df)


################################

import pandas as pd
import random
import numpy as np

df = pd.DataFrame({
    # "Date": pd.date_range(start="2026-07-01", periods=10, freq="D"),
    # "Salary": [random.randint(500, 1000) for _ in range(10)],
    # "Age": np.linspace(20, 60, 10).astype(int)
    "Date": pd.date_range(start="2026-07-07", periods=10, freq="D"),
    "Salary": [random.randint(1000, 2000) for _ in range(10)],
    "Age": np.linspace(3000, 4000, 10).astype(int)
})

print(df)


s = "learn python every day"

freq = {}

for ch in s:
    if ch == " ":
        continue

    if ch in freq:
        freq[ch] = freq.get(ch, 0) + 1
    else:
        freq[ch] = 1

print(dict(sorted(freq.items(), key=lambda freq: freq[1], reverse=True) ))
#print(dict(sorted(freq.items(), key=lambda freq: freq[0], reverse=False)))
        