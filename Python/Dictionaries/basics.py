#Thats a simple dictionary
simple_dict = {"name": "Michael", "age": 30, "hobbies": ["programming", "swimming", "drawing"]}
#A dictionary is a pair where KEY is associated with VALUE eg.: "name": "Michael"  

#The KEY can only be an immutable data type like string or int.
#The VALUE can be antyhing.
  
#A dictionary can be easly printed just with print function
print(simple_dict)

#We can print specific value inserting a KEY into square brackets.
print(simple_dict["name"]) #KEY:"name", VALUE: "Michael"

#But in our case last key "hobbies" has a list value. How we can print that?
#Treating a key as a list!
#This:
print(simple_dict["hobbies"][0])
#is equivalent to this:
list_of_hobbies = simple_dict["hobbies"]
print(list_of_hobbies[0])

#But what if we want to print a value with KEY that doesn't exist?
print(simple_dict["email"])
#We got an "KeyError" but its not an end of the world. Dictionaries have built in function
#to printing a values with keys. get() mehod which returns 'None' in case of wwrog key.
print(simple_dict.get("email")) 

#We can also assign a default value.
print(simple_dict.get("email","Key Not Found"))

#So... how can we insert new key-value pair into dictionary?
simple_dict["email"] = "blabla@test.com"
print(simple_dict["email"]) 

#If this key exited it would update the value.
simple_dict["name"] = "Bob"
print(simple_dict["name"])

#But we can update keys and values with... you guessed it, update() method.
#It takes in a dictionary of keys and values of everything we want to add or change value.
simple_dict.update({"name":"Charles","age": 31})
print(simple_dict)

#We can also delete a key value pair just just 'del' keyword.
del simple_dict["email"]
print("After deleting 'email' key from simple_dict")
print(simple_dict)

#If we want to delet and return a deleted value from key we can use a pop() method. (just like in case of Lists)
print("Dictionary before popping key")
print(simple_dict)

age = simple_dict.pop('age')
print(age)

print("And after popping key")
print(simple_dict)

#Just like with lists we can len() function to see how many keys are in dictionary.
print(len(simple_dict))

#We can print just keys using keys() method
print(simple_dict.keys())

#And we can print only values using values() method.
print(simple_dict.values())

#If we can see keys and values together we can use items()
print(simple_dict.items())

#This methond is usefull in looping through our dictionary.
for key, value in simple_dict.items():
    print(key, value) 