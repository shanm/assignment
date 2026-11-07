
import pandas as pd


emp = pd.DataFrame({
    "emp_id": [101, 102, 103, 104],
    "emp_name": ["John", "Alice", "Bob", "Eve"]
})

emp_salary = pd.DataFrame({
    "emp_id": [101, 102, 104],
    "salary": [50000, 60000, 55000]
})

df_inner = pd.merge(emp, emp_salary, on="emp_id")
df_left = pd.merge(emp, emp_salary, on="emp_id", how="left")
df_right = pd.merge(emp, emp_salary, on="emp_id", how="outer")

print("Inner Join:\n", df_inner)
print("Left Join:\n", df_left)
print("Right Join:\n", df_right)

result = []

for num in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(num)):
        result.append(str(num))

#print(",".join(result))


result = []
for num in range(1000, 3001):
    num = (int(digit) % 2 == 0 for digit in str(num))
    print(num)
    #if all(int(digit) % 2 == 0 for digit in str(num)):
    #    result.append(str(num))

print(",".join(result))


