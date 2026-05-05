#A dictionary is an unordered , changable, and indexed collection. Intead of things up by an index number (like 0,1,2,3...) in a list , we use a specific Key. 

"What is a Python Dictionary?"
#A dictionary is an unordered, changable , and indexed collection. It stores data in key-value pairs.
#Key: The unique identifier(like a word in a dictionary)
#value: The data associated with that key(like a word in dictionary)
#In python, dictionaries are written with curly brackets {}
#Basic Syntax 
# my_car = {
#     "Brand": "Mercedies",
#     "Model": "Benz", 
#     "Year" : 1990
# }

#Key characteristic of dictionary : 
#1) Unique keys: You cannot have two identical key. If you assign a new value to an existing key, the value is overwritten.
#2) Changable: You can add, remove, or change items after the dictionary is created. 
#3) DataTypes: Keys are usually strings or numbers, but value can be anything (integer, list, even other dictionaries)

#how to access and modify data
# my_car["Brand"] #accessing
# my_car["Brand"] = "Lambo" #modifing /Updating
# del my_car["Year"]
# print(my_car)

#Dictionary Methods & Looping
#essential dictionary methods 
# my_car = {
#     "Brand": "Mercedies",
#     "Model": "Benz", 
#     "Year" : 1990
# }
# print(my_car.keys()) #returns a list of all keys 
# print(my_car.values()) #retuns a list of all values 
# print(my_car.items()) #retuns key-value pair as tuples 
# print(my_car.get("math")) #safely gets a value (no erro if key is missing )
# print(my_car.clear()) #removes all items form the dictionary

#Looping Through a Dictionary 
#The most powerful way to handle dictionaries is using the .items() methos in a for loop. 
#This allows you to grab the key and the value at the same time . 

# student = {"Maths":95, "English": 88, "Science":90}
# for i,j in student.items():
#     print(f'I got {j} in {i}')

# Practice Quiz: Section 2
# 1. The Safe Access
# If you try to access a key that doesn't exist using my_dict["hidden_key"], Python throws a KeyError. Which method should you use instead to 
# return None (or a default message) instead of crashing?
# student = {"Maths":95, "English": 88, "Science":90}
# student.get("hidden_key")
#basically we we type to access the key , it throws an error so we use get method to access , and it returns a none value 



# 2. The Loop Challenge
# Write a simple for loop that prints only the values of this dictionary:
# inventory = {"apples": 10, "bananas": 5, "cherries": 15}.
# inventory = {"apples": 10, "bananas": 5, "cherries": 15}
# for fruits,quantity in inventory.items():
#     print( quantity)

# 3. Cleanup
# What single line of code would you use to delete every single item inside a dictionary named data without deleting the data variable itself?
# How do these look to you?]"
# inventory = {"apples": 10, "bananas": 5, "cherries": 15}
# inventory.clear()

#section 3:Nested Dictionaries & Dictionary Comprehension 
#This is where dictionaries get really powerful, you can put dictionaries inside dictionaries(Nesting) and create dictionaries using shorthand code(Comprehension)
#Nested Dictionaries 
#Think of this like a filing cabinet where each drawer is a dictionary, and inside each drawer, ther are more specific folders.

# users = {
#     "user1" : {"name":"John", "age":23}, 
#     "user2" : {"name":"Joseph", "age":21}
# }
# print(users["user1"]["age"])

#2)Dictionary Comprehension
#Just like List Co