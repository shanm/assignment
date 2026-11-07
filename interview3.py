l = [1, 2, 3, 4, 5, 6]
result = [i*i if i%2 == 0 else i for i in l]
print(result)

#######################

#Output = [1,2,3,4,5,6,7]
def flattern(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flattern(item))
        else:
            result.append(item)
    return result

l = [1,[2,3],[4],5,[6,7]]
print(flattern(l))

##################################
d = [
    {'name': 'David', 'age': 32},
    {'name': 'Tom', 'age': 24},
    {'name': 'John', 'age': 26}
]

result = sorted(d, key=lambda x: x['age'])
#result = sorted(d, key=lambda x: x['age'], reverse=True)

print(result)

#d.sort(key=lambda x: x['age'])
#print(d)

# def get_age(item):
#     return item['age']

# result = sorted(d, key=get_age)

####################################
def remove_sp(func):
    def wrapper(name):
        cleaned_name = ''.join(n for n in name if n.isalnum())
        return func(cleaned_name)
    return wrapper


@remove_sp    
def test(name):
    return name

print(test(“A@mantya!”))


