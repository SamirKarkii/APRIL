#Function helps to reuse code, organize code, save time, make programs cleaner 

#Basic of function
#phase one 
# def greet():
#     print("Welcome")
# greet()

# def school():
#     for i in range(1,4):
#         print("I am lerning PYthon")
# school() #It will print each three time 
# school()
# school()

# def music():
#     print("Yello")
# music()
# music()

# def morning():
#     print("Wake UP")
# def night():
#     print("Sleep")
# morning()
# night()

# def robot():
#     print("Booting... " 
#     "System Ready")
# robot()
# robot()
# robot()
# robot()
# robot()

#Phase 2 

#Function naming rules 
#be meaningful 
#be lowercase

# def tea():
#     print("Making Tea")

# def breakfast():
#     print("preaparing breakfast")
#     tea()

# breakfast()

# def study():
#     print("Studying Python")

# study()
# study()
# study()
# study()

# def open_door():
#     print("Open the door")

# def close_door():
#     print("Close the door")

# open_door()
# close_door()


# def engine():
#     print("Engine")

# def car():
#     print("Car")
#     engine()
# car()


# def wake_up():
#     print("wake up ")
# def brsh():
#     print("Brush Your teeth")
# def breakfast():
#     print("then have breakfast")

# def morning_routine():
#     wake_up()
#     brsh()
#     breakfast()
# morning_routine()

#Phase 3 (Parameter Vs Argument)

# def greet(name): # name is parameter 
#     print("Hello",name)

# greet("sam") #sam is an argument 


# def game(title): 
#     print(title,"Started")

# print("pubg")
# print("clash of clans")

# #multiple parameter 
# #function can take multiple parameter 

# def add(a,b): #here a, b is parameter 
#     print(a+b)

# add(1,3)#3 is an argument
# #parameter count must match
 

# def add(a,b):
#     print(a+b)
# add(b=2,a=1)


# def hello(name):
#     print("Hello",name)

# hello("Sam")

# def multiply(a,b):
#     print(a*b)
# multiply(10,10)


# def city(name):
#     print(f'Welcome to {name}')
# city("kathmandu")
# city("Pokhara ")


# def student(name,age):
#     print(f'Name:{name}')
#     print("Age:",age)

# student("sam's bro",19)


# def student(name,age):
#     print(f'Name:{name}')
#     print("Age:",age)

# student("sam's bro",19)


# def student(name="sam's bro",age= 19):
#     print(f'Name:{name}')
#     print("Age:",age)

# student()


# def power(base,exponent): 
#     print(base**exponent)
# power(2,10)

# def greet(name="Greet"):
#     print(name)
# greet()
# greet("Sam")


#Return value
#This is a massive topic , beginner often think print() and return are similar but they are not 

#Difference between print and return value
#print only display output doensnot sent a value back 

#return sends balue back to the caller , allows storing and reusing results 

# def add_with_print(a,b):
#     result = a+b
#     print(result)

# my_total = add_with_print(2,3)

# final_step =  my_total*10 #this will throw error 

# def add_with_return(a,b):
#     result = a+b
#     return result

# my_total = add_with_return(3,4)
# print(my_total+10)


def multiply(a,b):
    return a*b

result = multiply(2,3)
print(result)


def fullname(first,last):
    name = first+last
    return name

apple = fullname("samir","borther")
print(apple)
print(apple+"arc")


def cube(n):
    return n**3
total = cube(3)
print(total)

def login(username, password):
    if username=="admin" and password =="1234":
        return "Login sussc"
    else:
        return "Invalid "

creditiantles = login("admin","1234")
print(creditiantles)

# Difference between print() and return?
#print bascically is for displaying , while return actually allows to store and resuse restly


# What does return do?
#retuns sends back the value to caller and it immediately shuts downs the function
# What is None?
#when we use print the return value is none, as the variable just displaly the value not hold it , its like nothing
# Does code run after return?
#NO the code mmediately stops 
# Why is return more powerful than print()?
#because it allows to store and reuse 
# What happens if function has no return?
#it give none