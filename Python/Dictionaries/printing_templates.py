simple_dict = {'a': 1, 'b': 2, 'c': 3}

# Print all keys ================================================
for key in simple_dict.keys():
    print(f"Key: {key}")
# Or
for key in simple_dict:
    print(f"Key: {key}")

# Print all values ================================================
for value in simple_dict.values():
    print(f"Value: {value}")
# Or
for key in simple_dict:
    print(f"Value for key '{key}': {simple_dict[key]}")

# Print all keys and values ================================================
for key, value in simple_dict.items():
    print(f"Key: {key}, Value: {value}")

# Suppose we want to get to the value for key 'b'
key = 'b'
value = simple_dict.get(key)
print(f"Value for key '{key}': {value}")

# We can also use direct indexing if we are sure the key exists:
value = simple_dict[key]
print(f"Value for key '{key}': {value}")

# Suppose we want to get to just the key 'b' alone without value
key_to_find = 'b'
for key in simple_dict.keys():
    if key == key_to_find:
        print(f"Found key: {key}")
        break


nested_dict = {
    'first': {'a': 1, 'b': 2},
    'second': {'c': 3, 'd': 4}
}

# Print all keys and values ​​from nested dictionaries
for key, sub_dict in nested_dict.items():
    print(f"Outer Key: {key}")
    for sub_key, sub_value in sub_dict.items():
        print(f"  Inner Key: {sub_key}, Value: {sub_value}")


list_of_dicts = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4}
]

# Print all items in the dictionary list
for i, d in enumerate(list_of_dicts):
    print(f"Dictionary {i}:")
    for key, value in d.items():
        print(f"  Key: {key}, Value: {value}")

dict_with_lists = {
    'numbers': [1, 2, 3],
    'letters': ['a', 'b', 'c']
}

# Print all items from the lists contained in the dictionary
for key, value_list in dict_with_lists.items():
    print(f"Key: {key}")
    for item in value_list:
        print(f"  List Item: {item}")

complex_dict = {
    'group1': {'a': [1, 2, 3], 'b': [4, 5, 6]},
    'group2': {'c': [7, 8, 9], 'd': [10, 11, 12]}
}

# Print all elements from nested structures
for outer_key, sub_dict in complex_dict.items():
    print(f"Outer Key: {outer_key}")
    for sub_key, sub_list in sub_dict.items():
        print(f"  Inner Key: {sub_key}")
        for item in sub_list:
            print(f"    List Item: {item}")

# Print dictionary in a pretty way
def recursive_print(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + f"Key: {key}")
        if isinstance(value, dict):
            recursive_print(value, indent+1)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    recursive_print(item, indent+1)
                else:
                    print('  ' * (indent+1) + f"List Item: {item}")
        else:
            print('  ' * (indent+1) + f"Value: {value}")

recursive_print(complex_dict)
