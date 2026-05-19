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


# def multiply(a,b):
#     return a*b

# result = multiply(2,3)
# print(result)


# def fullname(first,last):
#     name = first+last
#     return name

# apple = fullname("samir","borther")
# print(apple)
# print(apple+"arc")


# def cube(n):
#     return n**3
# total = cube(3)
# print(total)

# def login(username, password):
#     if username=="admin" and password =="1234":
#         return "Login sussc"
#     else:
#         return "Invalid "

# creditiantles = login("admin","1234")
# print(creditiantles)

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


#Topic 5- Scope 
#this topic explians : 
#Scope is the region where a variable can be accessed or used.
#Local Scope 
#Global Scope

#Local Variables 
#a variable inside a function
# def test():
#     x=10
#     print(x)
# test() #basically x only exists inside tes 
# print(x) #Throws name error, because local variable dies after functions ends

#Global variable 
# name = "Sam"
# def show():
#     print(name)

# show() #global variable can be accessed inside function.


#combining both

# x =100
# def test():
#     x =50
#     print(x)
# test()
# print(x)


# # Task one
# def test():
#     x=50
#     print(x)

# # print(x) #name error because local variable dies after func ends

# #task two

# # country = "Nepal"
# # def show_country():
# #     print(country)
# # show_country()

# # #task 3
# # score =100
# # def match():
# #     score = 50
# #     print(score)

# # match() #this prints local variable 


# #*args basically allows a function to accept any number of positonal argument . 
# #*args collects multiple positional arguments into a tuple 

# # def number(*args):
# #     print(args)

# # number(2,3,4,4,5)

# def show(*agrs):
#     for item in agrs: 
#         print(item)

# show("apple", "ball", "football")

# #Real example sum of number 
# def total(*args):
#     sum = 0
#     for i in args: 
#         sum = sum+i
#     return sum

# print(total(2,3,4,5))

# #Mixing normal parameters + *args 

# def profile(name,*args):  #normal parameter comes first 
#     print(name)
#     print(args)

# profile("Sam","Python", "Djanog", "Docker", "Postgres")



# #Task one:
# def friends(*args):
#     print(args)
# friends("Sam","Ram","Harry")
# friends("Sam","Ram","Harry","alex", "ramhari")

# #Task Two : 
# def multiply(*numbers):
#     mul = 1
#     for i in numbers:
#         mul = mul*i
#     print(mul)

# multiply(2,3,4)

# #Task three:
# def student(name, *marks): 
#     print(name)
#     print(marks)

# student("Alex", 10,20,30,40,50)

# #Task 4 
# def highest(*nums):
#     return max(nums)
# print(highest(2,3,4))

# #Task 5: 
# def info(valur,*data):
#     for i in data:
#         print(i,valur)
# info("$",1,2,3,4,5,)


#**kwargs 
# **kwargs collects multiple keyword arguments into a dictionary 

def info(**kwargs): 
    print(kwargs)  #inside a function **kwargs becomes a dictonary, key--> vlaue pairs 

info(name="samir", age= "19", gender= "male") 

#loopng through, kwargs

def loopexample(**kwargs): 
    for key,value in kwargs.items(): 
        print(key, "=", value)

loopexample(name="samir", age="19", gender= "male")

#normal parameter +  **kwargs 
def student(name, **details): 
    print(name)
    print(details)

student("Samir", age="19", city ="kathmandu")

def test(**kwargs):
    print(kwargs)
test(name="Gaara", age =21)

def data(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
data(city="Kathmandu", country = "Nepal")

#Task one  and two
def user(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)
user(name="sam", age=22, country = "Nepal")

#Task three
def product(**details):
    print(details)
product(name="grapes", price=100, stock=7)

#Task four 
def profile(name,**kwargs):
    print(name)
    print(kwargs)

profile("Sam", age=21,work="backend developer")

#Task five 
def setting(**options): 
    return len(options)

print(setting(name="one",name1="tow", name3="three"))

#Challenge Task : 
def game(character, **power):
    print("character: ",character)
    for i,j in power.items():
        print(i,"=",j)
game("ninja", speed=100, strenth=80, stealth=99)