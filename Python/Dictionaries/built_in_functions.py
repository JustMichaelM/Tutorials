simple_dict = {"name": "Michael", "age": 30, "hobbies": ["programming", "swimming", "drawing"]}

#======== Built In Methods ============
#In case of additional help:
#print(dir(simple_dict))
#print(help(simple_dict))

# 1. values()
print(simple_dict.values()) # returns iterable of values

# 2. keys()
print(simple_dict.keys()) # returns iterable of keys

# 3. pop()
popped = simple_dict.pop("age") # deleting a key and returning a value assigned to this key
print(simple_dict)
print("value of variable popped: ",popped)

# 4. popitem()
print(simple_dict)
popped = simple_dict.popitem() #Just like pop() but last item of the dictionary
print(popped)
print(simple_dict)

# 5. copy()
example_dict = {0: ["a","b"], 1:["c","d"], 2: "Cat"}

other_dict = {}
other_dict = example_dict.copy() # return a SHALLOW copy of dictionary which means that a dictionary is
#in its own memory adress but MUTABLE variables inside dont and are shared by all copies and original dictionary.

other_dict[0][0] = "xyz"
print(other_dict)
print(example_dict)

#Ofcourse with immutables there's no problem.
other_dict[2] = "Dog"
print(other_dict[2])
print(example_dict[2])

# 6. get()
print(simple_dict.get('name')) # another way to returning a value from key with twist of setting default value
#when key doesnt exist
print(simple_dict.get('address')) # Key doesn't exist so returns None
print(simple_dict.get("address","Not Found"))

# 7. setdefault()
print(simple_dict.setdefault("name"))
print(simple_dict.setdefault("address","some street 34")) #Similar to get() method but incase of key doesn't exist
# it inserts a new key-value pairn into dictionary 
print(simple_dict)

# 8. clear()
simple_dict.clear() #It clears entire dictionary. All keys and all values
print(simple_dict)

# 9. fromkeys()
#making a new dictionary from a list with default value of None
people = ["Jane","Bob","Charles"]
users = dict.fromkeys(people)
print(users)


# 10. items()
#returns a iterable list of key-value pairs
simple_dict = {"name": "Michael", "age": 30, "hobbies": ["programming", "swimming", "drawing"]}
print(simple_dict.items())

#We can use that to iterate through dictionary

for key, value in simple_dict.items():
    print(key, value)


# 11. update()
#Expands and/or modifies a existing dictionary. It takes a dictionary of keys and values you want to update or insert
print(simple_dict)
simple_dict.update({"name": "Jane", "phone": "123-456-789"}) #we modified name value and added new one: phone
print(simple_dict)

# ALTERNATE method to update dictionary
simple_dict = simple_dict | {"id": 123456}
simple_dict = simple_dict | {"name": "Bob"}
print(simple_dict)

# ALTERNATE printing dictionary using pprint module
import pprint

pprint.pp(simple_dict)