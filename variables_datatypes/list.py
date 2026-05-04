#list is a datastucture used to store collection of iteam into a single variable. Lists are incrediably versatile,making 
#them one of the most frequently used tools in python programming . 
#key characterists:
#ordered: Lists maintains the order in which items are inserted . The first item is at index 0, second at 1, ans so on.
#Mutable: You can change,add, or remove items after the list has been created.
#heterogeneous : A single list can contain different data types (eg, strings, integers, and even other list )
#Allow Duplicates: List can contain the same value multiple times. 

#basic sntac of list 
#we can create a list by placing elements inside square brackets [], seperated by commas. 
# number = [1,2,3]
# mixed = [10, "Hell0", 3.1, True]

# #common list operation 
# a = [1,2,3 ]
# #accessing - access an item by its index 
# a[0]
# #appending- adds an item at the end of list 
# a.append(4)
# #inserting - adds an item at a specific index 
# a.insert(1,3)
# #removing - removes the first occurence of list .
# a.remove(2)
# #length - returns the number of items in list. 
# len(a)
# #slicing - returns a new list containing a subset of items. 
# a[0:2]

#main important concepts of list : 
#slicing,nested list , iteration 

# Challenge 1: Slicing
# Given the following list, write code to extract the specific segments requested.
# Python
# data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Task A: Extract the first three elements using slicing.
# Task B: Extract only the middle three elements (40, 50, 60).
# Task C: Use a negative step to reverse the entire list.

# data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(data[0:3:1])
# print(data[3:6:1])
# print(data[::-1])

# Level 1: Basics (Forward)
# Extract [20, 30, 40].
# Extract everything from index 5 to the end.
# Extract every second element from the entire list ([0, 20, 40, 60, 80]).
# nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[2:5])
# print(nums[5::1])
# print(nums[::2])

# Level 2: The "Negative" Mindset
# Extract the last 3 elements using negative indexing: [70, 80, 90].
# Extract the list excluding the first and last elements: [10, 20, 30, 40, 50, 60, 70, 80].
# Extract only [60, 40, 20] (This requires a negative step and careful start/stop points).
# nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[:6:-1]) #num[-3:]
# print(nums[1:9:1])
# print(nums[6:1:-2])

# #extract the llist stating from index 7 backwards to index 2: 
# print(nums[7:1:-1]) #extracting values from 7 to 2 index if stop was at 2, it will skip 20 

#Can you write a slice that produces an empty list [] without usign start or stop values that are outside the range
#It will likey say index out of range, if we try to index somthing thats not there in the list 

#A nested list is simply a list that contains other lists as its elements. You can think of it like a folder that contains 
#subfolders, or a table with rows and columns.

# matrix = [[1,2,3],
#         [4,5,6],
#           [7,8,9]]
#Accessing Elements: (The "Double Bracket"Rule): Because you have a list inside a list, you need two sets of indices 
#to pinpint a specific item 
#the first index targets the sub-list (the row)
#the second index targets the item inside the sub-list(the column)

#example to get the number 5 from the matrix above: 
#* matrix[1] gets you the second list [4,5,6].
#* matrix[1][1] gets you the element at index 1 of that list, which is 5.

#Flexibility : Nested lists don't have to be perfect squares or grids. You can have sub-lists of different lengths, or 
#even mix single items with sub-lists. 
# ronny = [[1,2],[1,0,4],[1]]

# Challenge: Nested Lists
# Use this list for the following questions:
    # Python
# classroom = [
#     ["Alice", "Bob", "Charlie"], # Group 1
#     ["David", "Eve"],            # Group 2
#     ["Frank", "Grace", "Heidi"]  # Group 3
# ]
# Task 1: Accessing
# Write the code to print "Charlie".
# Write the code to print "Grace".
# print(classroom[0][2])
# print(classroom[2][1])

# Task 2: Modifying
# Replace "Bob" with "Bobby" in the first group.
# Add a new student "Ivan" to the end of the second group (Hint: append works on the sub-list)
# classroom.insert([0][1, "Bobby"])


# classroom = [
#     ["Alice", "Bob", "Charlie"],
#     ["David", "Grace", "Heidi"], 
#     ["Frank", "Grace", "Heidi"]
# ]

# print(classroom[0][2])
# classroom[0][1] = "Bobby"
# print(classroom)
# classroom[1].append("Ivan")
# print(classroom)

#Question Number-3 
# menu = [["coffee","tea"],
#         ["cookie","cake"]]
# print(menu[1][0])

#Iteration is the process of repeating an action over and over again. In programming, specifically with lists, it means taking 
#a list and "visiting" every single item one by one to persorm a task . 
#think of it like a teacher handingout snaks to a row of student, give a snack, move to second student , givee a snack, ans so on, 
#until they reach the end of the row .

#In python, we use the for loop to iterate. It is the most common and "readable" way to go through a list.

# a = ["apple", "banana", "Cherry"]
# for i in a: 
#     print(i)

#Iterating through nester lists:
#Since , we now know about nested list, iterating through them is just one step more advanced. You use a nesed loop (a loop inside a looop), 

# classroom = [["apple, banana","grapes"], ["mango", "papaya"]]
# for i in classroom: 
#     for j in i: 
#         print(j)


"Question Number 1 "
# shopping_cart = [
#     ["Milk", "Bread", "Eggs"],
#     ["Apples", "Oranges"],
#     ["Chicken", "Rice"]

# ]
# for i in shopping_cart: 
#     print(i)

# "Question Number 2 "
# shopping_cart = [
#     ["Milk", "Bread", "Eggs"],
#     ["Apples", "Oranges"],
#     ["Chicken", "Rice"]

# ]
# total_items = 0
# for i in shopping_cart: 
#     for j in i: 
#         print(j)
#         total_items = total_items + 1

# print(f'The total number of item is: {total_items}')

# "Question Number 3 "
# shopping_cart = [
#     ["Milk", "Bread", "Eggs"],
#     ["Apples", "Oranges"],
#     ["Chicken", "Rice"]
# ]
# for i in shopping_cart: 
#     for j in i:
#         if j == "Milk":
#             print("Found the milk!")
#         else: 
#             print(f'this is something else: {j}')

#We need to bridge the gap between user input (which is always a string) and a list of number(which we can do math with : )
#Since users usually type nymbers separated by spaces (eg, 1 2 3 4) , her is the step by- step breakdown to turn that into a sum. 

# a = input("Enter numbers seperated by space")
# a = a.split()
# total = 0 
# for i in a: 
#     number = int(i)
#     total = total+ number
# print(total)

# Asks the user for a list of items (some numbers, some words) separated by spaces.
# Uses split() to create a list.
# Calculates the sum of only the numbers in that list.
# Prints the sum AND a count of how many items were "skipped" (the words).

"Question Number 1"
# user = input("Enter a number seperated by spaces: ")
# user_split = user.split()
# total = 0 
# for i in user_split: 
#     number = int(i)
#     total = total+ number
# print(total)

# "Question Number 2"
# user = [1,4,5,6,7,9,2]
# max = user[0]
# for i in user: 
#     if i>max :
#         max =i
        
# print(max)


"Question Number 4 "
# 4. Search an Element
# Take a list and a number
# Print:
# "Found" if present
# "Not Found" if not
# a = [1,2,3,4,5,9,7,10]
# for i in a: 
#     if i==3: 
#         print("Is present")
#         break
#     else:
#         print("Not found")

# "Question NO.5"
# Input=  [1,2,2,3,2]
# count = 0
# for i in Input:
#     if i==2:
#         count = count+1
# print(count)

# "Question NO.6"
# a = [1,2,3,4,5]
# x=2
# for i in a: 
#     if i>x:
#         print(i)
# "another approach "
# a = [1,2,3,4,5]
# for i in a: 
#     if i>a[0]:
#         print(i)

#In python , True and False are boolean values used to control flow of your program. They are the results of comparisions and logical 
#operations, and they determine which blocks of code are executed within if, elif, and else statement. 

# is_raining = True
# if is_raining: 
#     print("Take an umbrella")
# else: 
#     print("Its a sunny day mate ")

#Most often , you generate True or False values by comparing variables using operators 

# age = 20 
# has_id = True
# if age>=18 and has_id:
#     print("Access Granted")
# else: 
#     print("Access denied ")

#Truthy and Falsy Values : 
#In python, you don't always need to explicitly compare values to True or False . many objects have an inherent boolean value: 
#False : 0, None , empty sequences/collections("", [], {},())

# user_input = input("Enter name:")

# if user_input: 
#     print(f'hello, {user_input}')
# else:
#     print("You didn't eneter a name ")


# a = [1,2,3,4,5,6,7,8,9]
# flag = False
# for i in a: 
#     if i==10:
#         flag = True
#         break
# if flag: 
#     print("Found")
# else:
#     print("Not found")

# a = [1, 2, 3, 4, 5]

# for i in a:
#     if i == 3:
#         print("Found!")
#         break
# else:
#     print("Not Found!")

# Take a list and a number
# 👉 Print the index of the element
# 👉 If not found → print -1
# Example:
# Input: [10, 20, 30, 40], target = 30  
# Output: 2

# a = [1,2,3,4,5,6]
# b = a[0]
# for i in a: 
#     if i==b:
#         break
# else: 
#     print(-1)

# 2. First Even Number
# Find the first even number in the list
# 👉 Print the number
# 👉 If none → a print "No even number"

# a = [10,20,30,40,50]
# for index in range(len(a)):
#     if a[index]==30: 
#         print(index)
#         break
# else:
#     print("-1")


# 👉 Q3: Last Occurrence
# Example:
# [1,2,3,2,4], target = 2 → output: 3
# 💡 Hint:
# Don’t break immediately
# Keep updating index

# user = [1,2,3,2,4]
# last_index = -1
# for index in range(len(user)):
#    if user[index] == 2:
#       last_index = index
# print(last_index)

a = [1,2,3,4,5]
for i in a: 
    if i>i+1:
        print("Not ascending")
else: 
    print(f'{a} is in ascendign order')