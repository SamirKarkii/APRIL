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
#Just like List Comprehsion , this is a "one-liner " way to create dictionaries . 
#Syntx : {key:value for item in iterable }

# a = {x:x+1 for x  in range(1,10)}
# print(a)


# company = {
#     "emp1": {"name": "Alice", "location": "New York"},
#     "emp2": {"name": "Bob", "location": "London"}
# }
# print(company["emp2"]["location"])

# 2. The Transformer
# I have a list of names: names = ["Apple", "Banana", "Cherry"].
# Use Dictionary Comprehension to create a dictionary where the key is the name and the value is the length of that name.
# (Hint: Use the len() function).

#Dictionary comprehension looks a bit intimidating at first because it packs a lot inoto one line. 
#Instead of writing 4 lines of code, we write 1.

# name = ["Apple","Banana"]
# name_length = {}
# for i in name:
#     name_length[i] = len(i)
# print(name_length)

# #Comprehensive Style: 
# name = ["Apple", "Banana"]
# name_length = {x:len(x) for x in name}
# print(name_length)

# nums = [1,2,3]
# num_sum = {x:x+10 for x in nums}
# print(num_sum)

# names = ["Python", "Java", "C"]
# programmin_languages = {x:"langu"age" for x in names}
# print(programmin_languages)

# company = {
#     "emp1":{"name":"Alice","location":"NewYork"}, 
#     "emp2":{"name":"Bob","location":"London"}
# }
# print(company["emp2"]["location"])

# 2. The Membership Check
# If you want to see if a key exists in a dictionary (to avoid errors), Python has a very "English-like" keyword for it.
# Fill in the blank:
# Python
# product = {"name": "Laptop", "price": 999}
# for i in product.keys():
#     if "price" == i:
#         print("Price is available")

# product = {"name":"Laptop", "price":99}
# if "price" in product: 
#     print("Available ")

#Union Operator in python 
# dict1 = {"apple":1, "ball":2}
# dict2 = {"mango":7, "bat":2}
# merge = dict1|dict2
# print(merge)

d = {"a": 10, "b": 20}
d["b"] = 100
print(d) 

#2. The Ghost Key
#How do you check if the key "email" exists in a dictionary called user_profile? (Use the "English-like" keyword).
user_profile = {"name":"Samir Karki", "email":""}
if "email" in user_profile: 
    print("exist")

#3. The Safeway
#Use the .get() method to look for a key called "phone" in user_profile.
#  If it's not there, make it return the string "Not Found"

#4. The Loop (Keys Only)
#Write a for loop that prints only the keys of the dictionary stock = {"Apple": 50, "Orange": 30}.
stock = {"Apple": 50, "Orange": 30}
for i,j in stock.items():
    print(i)
    
stock = {"Apple": 50, "Orange": 30}
for i,j in stock.items():
    print(j) 


#6. Adding on the Fly
#You have colors = {"red": "#FF0000"}. Write one line to add "blue" with the value "#0000FF".
colors = {"red": "#FF0000"}
colors["blue"]="#0000FF"
print(colors)

#7. The Counter (Logic)
#If points = {"player1": 5}, how do you add 10 more points to player1 so their new total is 15?
points = {"player1":5}
points["player1"] +=10
print(points)

#8. The Dictionary Factory (Comprehension)
#Use dictionary comprehension to create a dictionary where the keys are numbers 1, 2, 3 and the values are those numbers 
#multiplied by 10 (e.g., {1: 10, 2: 20...}).
a =[1,2,3,4,5,6]
b = {x:x*10 for x in a}
print(b)

#9. The Deep Dive (Nesting)
#Given: data = {"users": {"id_1": "Alice", "id_2": "Bob"}}. Write the code to print the name "Bob".
data = {"users": {"id_1": "Alice", "id_2": "Bob"}}
d=data["users"]["id_2"]
print(d)

#10. The Big Cleanup
#What is the difference between del my_dict["key"] and my_dict.clear()?
#del will delete a particular give key  while clear removes everything