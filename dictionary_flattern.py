def flatten_dict(d, parent_key="", sep="."):
    items = {}

    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep))
        else:
            items[new_key] = value

    return items

def print_nested(d):
    for key, value in d.items():
        if isinstance(value, dict):
            print_nested(value)
        else:
            print(f"{key} : {value}")

data = {
    "user": {
        "name": "Mike",
        "address": {
            "city": "N.Y"
        }
    }
}

flat = flatten_dict(data)

print(flat)
print_nested(data)

############################
def print_paths(d, path=""):
    for key, value in d.items():
        current = f"{path}.{key}" if path else key

        if isinstance(value, dict):
            print_paths(value, current)
        else:
            print(f"{current} : {value}")

print_paths(data)