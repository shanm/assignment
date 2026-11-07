# How to remove the duplicates from the List of Dictionaries in Python?
list_of_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Bob", "age": 30}
]

seen = set()
unique_dicts = []

for d in list_of_dicts:
    unique_tuple = tuple(d.items())

    if unique_tuple not in seen:
        seen.add(unique_tuple)
        unique_dicts.append(d)

print(unique_dicts)

#################################
list_of_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Bob", "age": 30}
]

unique_dicts = [dict(item) for item in set(tuple(d.items()) for d in list_of_dicts)]
print(unique_dicts)
