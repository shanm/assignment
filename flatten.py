def flattern(arr):
    result = []
    for item in arr:
        if isinstance(item, (list, tuple)):
            result.extend(flattern(item))
        else:
            result.append(item)
    return result


print(flattern([1, [2, [3, [4,5]]], 6, [7,8,[9]]]))
