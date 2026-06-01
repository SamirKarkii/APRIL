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


# #**kwargs 
# # **kwargs collects multiple keyword arguments into a dictionary 

# def info(**kwargs): 
#     print(kwargs)  #inside a function **kwargs becomes a dictonary, key--> vlaue pairs 

# info(name="samir", age= "19", gender= "male") 

# #loopng through, kwargs

# def loopexample(**kwargs): 
#     for key,value in kwargs.items(): 
#         print(key, "=", value)

# loopexample(name="samir", age="19", gender= "male")

# #normal parameter +  **kwargs 
# def student(name, **details): 
#     print(name)
#     print(details)

# student("Samir", age="19", city ="kathmandu")

# def test(**kwargs):
#     print(kwargs)
# test(name="Gaara", age =21)

# def data(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
# data(city="Kathmandu", country = "Nepal")

# #Task one  and two
# def user(**kwargs):
#     print(kwargs)
#     for i,j in kwargs.items():
#         print(i,j)
# user(name="sam", age=22, country = "Nepal")

# #Task three
# def product(**details):
#     print(details)
# product(name="grapes", price=100, stock=7)

# #Task four 
# def profile(name,**kwargs):
#     print(name)
#     print(kwargs)

# profile("Sam", age=21,work="backend developer")

# #Task five 
# def setting(**options): 
#     return len(options)

# print(setting(name="one",name1="tow", name3="three"))

# #Challenge Task : 
# def game(character, **power):
#     print("character: ",character)
#     for i,j in power.items():
#         print(i,"=",j)
# game("ninja", speed=100, strenth=80, stealth=99)



# What does **kwargs do?
#keyword argument is used to handle multiple keyword argument
# What type is kwargs?
#dictionary
# Difference between *args and **kwargs?
#one is postional and one is keyword
# Why are two stars needed?
#if no star just a normal parmaeter, if one args, if two then kwargs
# Can kwargs be renamed?
#yes ofc 
# Why use kwargs instead of fixed parameters?
#for flexibility


#Multiple return values 
#unitl now only one return value but python allows many return value together.
#This becomes extremely useful for : calculations, APIs, game systems, data processing, machine learning 

#Python function can return multiple values seperated by commas. 

# #Basic example; 
# def calc(a,b): 
#     return a+b, a-b
# #what actually happens , python secreately pack it into : a tuple, so this becomes rertun (a+b,a-b)


# #Receiving Multiple values 
# x,y,= calc(10,5) #number of variables should usallymatch returned values 
# print(x)
# print(y)

# def student():
#     return "Sam", 19, "Nepal"

# name, age , country = student()
# print(name)
# print(age)
# print(country)

# #returning tuple directly
# def data():
#     return 1,2,3

# x = data()
# print(x)


# #Why multiple returns are useful instead of writing multiple function , it can return everything in one function

# def operation(a,b):
#     return a+b,a-b,a*b,a/b

# add,subtract,multiply,divide = operation(10,5)
# print(add)
# print(subtract)
# print(multiply)
# print(divide)



# #Task one
# def math(a,b):
#     return a+b, a*b

# add,mul = math(3,1)
# print(add)
# print(mul)

# #Task two 
# def user():
#     return "Samir", 21, "NP"
# name,age,country = user()
# print(name)
# print(age)
# print(country)

# #Task three 
# def rectangele(length,width): 
#     return length*width, 2*(length+width)

# area,peremeter = rectangele(10,5)
# print(area)
# print(peremeter)

# #Task four 
# def marks(a,b,c):
#     return a+b+c, (a+b+c)/3

# total,average = marks(5,4,3)
# print(total)
# print(average)

# #Task five 
 

# def stats(numbers):
#     return max(numbers), min(numbers), sum(numbers)

# maximum, minimum, total = stats([1,3,4,5,9])


# #challenge 
# def game_stats(a,b,c,d):
#     return a,b,c,d

# health,aromor,coins,level = game_stats(100,50,250,7)
# print(f'Health:{health}')


#theory qna 
# Can Python return multiple values?
#yes
# What data structure is actually returned?
#tuple
# Why are multiple returns useful?
#we don't have to use multiple func, the work can be done with one
# What happens if variables don’t match returned values?
#error
# What happens if single variable stores multiple returns?
#stores tuple 


#Nested Function
#function inside a function 
#basically a nested function is a function defined inside another function 4

# def outer(): 
#     def inner(): 
#         print("Inner function ")
#     inner()

# outer()


# def calculate(a,b): 
#     def add(): 
#         return a+b
#     def multiply():
#         return a*b
#     print(add())
#     print(multiply())

# calculate(2,4)

# #Inner function can access outer function variables.

# def outer():
#     name = "Samir"

#     def innner():
#         print(name)
#     innner()

# outer()

# #Nested return example

# def outer():
#     def inner(): 
#         return "Hello"
#     return inner()
# print(outer())


# def greet(): 
#     return "Hello"

# my_variable = greet 
# my_result = greet()
# print(my_variable())
# print(my_result)


# def outer_function(): 
#     print("outer")

#     def inner_function():
#         print("inner")
#     return inner_function

# outer_function()()



# def kitchen():
#     print("Step 1: Kitchen is open!")
    
#     def bake_cake():
#         print("Step 2: Cake is baked! 🎂")
        
#     return bake_cake

# a = kitchen()
# a()


# #Task 1 
# def school():
#     def student(): 
#         print("Student Studying")
#     student()

# school()

# #Task 2 
# def outer():
#     game = "Chess"
#     def inner():
#         print(game)
#     inner()
# outer()

# #Task three
# def math(a,b):
#     def add(): 
#         return a+b
#     def mul(): 
#         return a*b
#     print(add())
#     print(mul())

# math(4,4)

# #Task 4: 
# def outer(): 
#     def inner(): 
#         print("Inner function")
#     return inner()
# outer()

# #Task 5 
# def outer(a=2,b=9): 
#     def inner(): 
#         return a+b
#     return inner()

# a = outer()
# print(a)

# #Challenge Task : 

# def login_system(username): 
#     def welcome(): 
#         if username == "admin": 
#             print("Welcome admin")
#         else:
#             print("Access denied")
#     welcome()

# login_system("admin")


#function inside another function is basically nested function
#no innner function can't be accessed outside 
#yes innerfun , can access outer variables
#return inner means just a funct name and it need to be called later, while return inner() means actual functiion calling 
#nested function is used to hide certain data, it is used in decorators , closures ,so on 



#Recursion
#Recursion is when a funcion calls itself. 

# def example(): 
#     print("When a function calls itself it is basically know as recursion")
#     example()
# # example()  #this weill lead to infinite loop and eventually, a recursion error , because function keeps calling itself forever, python eventually stops it


# #Every recursion function must have, a stopping condion , otherwise recursion never ends . 
# #This stopping condition is called a base case . 

# #Core Sturcture of Recursion : 
# #Every recursive function has two parts:
# #1) Base case: Stops recursion. 
# #2) Recursive Case: Function calls it self 

# def countdown(n): 
#     if n==0: 
#         print("Done")
#         return 
#     print(n)
#     countdown(n-1)

# countdown(5)

# #Important understanding, recursive calls create, new function frames, each call is seperate
# #Python remembers : current value , current position, current execution state, this uses: call stack 

# def factorial(n): 
#     if n==1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))


# def sum(n): 
#     if n==1: 
#         return 1
    
#     return n + sum(n-1)

# print(sum(5))


# def repeat(text,n): 

#     if n==0: 
#         return 
#     print(text)

#     repeat(text,n-1)

# repeat("PYTHON", 3)


# #Task One 
# def count(n): 
#     if n==6:
#         return 
#     print(n)
#     return count(n+1)
    
# print(count(1))


# #Task two 
# def sum_numbers(n):
#     if n==1: 
#         return 1
#     return n+sum_numbers(n-1)

# print(sum_numbers(5))

# #Task three 
# def factorial(n): 
#     if n==1: 
#         return 1 
#     return n*factorial(n-1)
# print(factorial(5))

# #Task four 
# def reverse_count(n): 
#     if n==0: 
#         return
#     print(n)

#     return reverse_count(n-1)

# reverse_count(5)

# #Task 5, left  power(base,exponent)

# #Challenge Task
# def login(attempts): 
#     if attempts==0:
#         print("Account Locked")
#         return
#     print(f'{attempts} attempts left')
        
#     return login(attempts-1)  

# login(5)



#Questions : 
# What is recursion?
#when a function calls itself 
# What is base case?
#stooping case 
# Why is base case important?
#to avoid infinite loop 
# What causes RecursionError?
#when we don't give base condition and it goes infinite and eventually crash 
# Difference between recursive case and base case?
#function calling itself vs stopping point
# What happens if recursion never stops?
#recursive error 


#Lambda Functions in Python
#A Lambda function is a small anonymous function defined in a single line 
#why anonynomous , because it has no name, used for short, quick operations. 

# #Normal function 
# def add(a,b): 
#     return a+b

# #Lambda version: 
# lambda a,b : a+b

# #key Syntax 
# # lambda argument: expression 
# #Important rules: 
# #1) Only one expression 
# #2) no return keyword 
# #3) automatically returns result 

# add = lambda a,b:a+b
# print(add(2,3))

# square = lambda x: x*x 
# print(square(4))

# #Immediate execution 
# print((lambda x: x+10)(5))

# #Important limitation : 
# #Lambda cannot: use multiple lines, use loops, use complex logic, use multiple statemate (It is only for simple expressions.)

# #where lamda is actually used, it is not usually used alone , it is used inside function like: 

# #1)map()
# num = [1,2,3,4]
# result  = list(map(lambda x: x*2,num))
# print(result)

# #2) filter 
# nums = [1,2,3,4,5,6]
# even = list(filter(lambda x: x%2==0, nums))
# print(even)

# #Task one 
# multiply = lambda x,y : x*y
# print(multiply(2,3))

# #Task two 
# print((lambda x: x*x*x)(5))

# #Task three: 
# a = [1,2,3,4,5,6,7]
# odd = list(filter(lambda x:x%2!=0,a))
# print(odd)

# b = [1,2,3,4,5,10,15]
# r = list(filter(lambda x:x>=10,b))
# print(r)

#First Class Function 
#In Python, a functions are first class citizens , meaning they can be : stored in variable, passed as argruments, returned from other function just like 
#normal values 

# x = 10 
# #but python also allows to store 
# x = greet #store funciton 
#that's first calls function


# #Storing Function in Variable 
# def hello(): 
#     print("This is an example of first class function ")
# x = hello  #this stores function itself not result   #x=hello(), this calls function immediately big difference 
# x()

# #Passing Function as Argument 
# def greet(): 
#     print("Hello Mate")

# def exexute(func): 
#     func()

# exexute(greet)


# #Returning Function 
# def outer():
#     def inner(): 
#         print("Inner")
#     return inner

# x = outer()
# x()

# #Multiple function : 

# def add(a,b): 
#     return a+b

# def subtract(a,b): 
#     return a-b

# def calculate(func,x,y):
#     return func(x,y)

# print(calculate(add,10,5))
# print(calculate(subtract,9,9))

# #first class function matter because it if foundation for decorators, callbacks ,event systems, frameworks,functional programming

# #Task one : 
# def greet():
#     print("Hello")

# x = greet 
# x()

# #Task two 
# def shout():
#     print("whho ha ha ")

# def execute(func): 
#     return func()
# execute(shout)

# #Task three 
# def add(a,b): 
#     return a+b

# def calculator(func,a,b): 
#     return func(a,b)

# calculator(add,2,3) #we can print this too but haven't used print as of now 

# #Task four 
# def a(): 
#     print("A")
    
# def b(): 
#     return a

# b()()

# #Task five : 

# def choose(option):

#     if option == "add":
#         return add

#     return subtract

# x = choose("add")

# print(x(2,3))


# #Challenge Task :
# def greet(): 
#     print("Hello")
#     print("Finished")


# def logger(func): 
#     print("Starting..")
#     func()

# logger(greet)

# What are first-class functions?
#a function which can be stored as variabled , passed as argu, and returned from another func
# Difference between:
# x = hello
#just storing function
# and
# x = hello()
#actually executes the function 
# Can functions be passed as arguments?
#yes 
# Can functions return other functions?
#yes
# Why are first-class functions important?
#without it decorators, higherorder function is not possible at all 


#Higher Order Function:
#A higher order function is a function , that takes another function as argument or returns another function ,sometimes both

# def greet(): 
#     print("Hello")

# def runner(func):  #why higher order function because runner(), accepts function.
#     func()

# runner(greet)

# #Calculator pattern 
# #why this is powerful , instead of writing add_num(), mul_num(), one generic function can works with many operation 
# def add(a,b): 
#     return a+b
# def mul(a,b): 
#     return a*b

# def calculator(operation,x,y): 
#     return (operation(x,y))

# print(calculator(add,2,3))
# print(calculator(mul,5,6)) 

# #Returning Function 

# def choose(operation): 

#     def add(a,b): 
#         return a+b
#     def sub(a,b): 
#         return a-b
#     if operation == "add": 
#         return add
#     return sub

# x =  choose("add")
# print(x(1,4))

# #We have already used higher order function before as we have used map(), filter() 
# num = [1,2,3,4,5]
# result = list(map(lambda x : x*2, num))# becuae map() function takes another function lambda 


# num = [1,2,3,4,5,6,7]
# result = list(filter(lambda x: x%2==0,num)) #even here filter(), takes lambda so it HOF. 

 

# #Callback Concept 
# #A callback is a function passed into another function to run later. 
# def done(): 
#     print("Finished")

# def process(callback): 
#     print("Processing..")
#     return callback()

# process(done)

# #Task one: 
# def welcome(): 
#     print("welcome")

# def execute(func): 
#     return func()

# execute(welcome)

# #Task two 
# def square(n): 
#     return n*n

# def apply(func,value): 
#     return func(value)

# apply(square,5)

# #Task three 
# def add(a,b): 
#     return a+b
# def mul(a,b): 
#     return a+b

# def calcluator(func,x,y): 
#     return func(x,y)
# calcluator(add,5,6)

# #Task 4 
# def choose(option): 
#     def add(a,b):
#         return a+b
#     def sub(a,b): 
#         return a-b
    
#     if option == "add": 
#         return add
#     return sub

# x = choose("add")
# print(x(1,2))

# #Task five
# def logger(func): 
#     print("Starting")
#     func()

# def wrapper(): 
#     print("Finished")
# logger(wrapper)


#Decorators
#Decorators is basically a tool that allow you to add new functionality, without changing its actual code. 

# #Baisc decorator
# def wrap_gift(original_func): 
#     def wrapper(): 
#         print("Putting a beautiful wrapping paper . . .")
#         original_func()
#         print("Attaching a nice bow !")
#     return wrapper 

# @wrap_gift
# def give_gift(): 
#     print("Here is you laptop mate! . . . ")
# give_gift()

# #why decorator exits: 
# #Imagive you have: "
# def login(): 
#     print("User logged in !")
# #Now we want, before every function runs, print starting 
# #We can do: 
# def login(): 
#     print("Starting...")
#     print("User logged in")
# #but for 
# def register(): 
#     print("Starting..")
#     print("User registered")

# def logout(): 
#     print("Starting. . .")
#     print("User logged out!")

# #The problem is we are repeating the same code again & again. 
# #Decorator basically solves this, instead of modifying every function, we create one wrapper 

# #Foundation : 
# def logger(function): #this is techincally a decorator 
#     def wrapper(): #it is a nested function
#         print("Starting")
#         function()
#         print("finished")
#     return wrapper #returns wrapper 

# # def greet(): 
# #     print("Hello world")

# # new_func = logger(greet)
# # new_func()

# #Python gives shortcut syntax fot this : 
# @logger
# def greet(): 
#     print("Hello world")
# greet()

# #What does @logger mean? 
# #python secretly does: 
# #greet = logger(greet)
# #this is the most importand decorator fact 

# #Task one: 
# def decorator(func): 
#     def wrapper(): 
#         print("Before")
#         func()
#     return wrapper

# def greet(): 
#     print("After")

# x = decorator(greet)
# x()

# #Task two 
# def decorator(func):
#     def wrapper(): 
#         print("1.2.3 Check!")
#         func()
#     return wrapper

# @decorator
# def greet(): 
#     print("4.5.6 Check!")
# greet()

# #Task four: 
# def logger(func): 
#     def wrapper(): 
#         print("Starting. . . ")
#         func()
#         print("Finished , yet I didn't get question no.3 ")
#     return wrapper

# @logger
# def confused(): 
#     print("Running function")

# confused()

# #Task five: 
# # @logger
# # def greet():
# =
# greet= logger(great)


# What is a decorator?
# #adding new functionality to an exisiting function without chaning its actual code
# Why do decorators exist?
# #to reduce the repetation of same code again and again
# What does @decorator actually do?
# #basically it adds extra functionality to an existing func
# Why are decorators useful in backend frameworks?
# #for maning routes , less code more organized workflow
# What are the three function concepts that make decorators possible?
# #nested , retuing function, higher order function , even first 



#Decorator with Arguments(*args,**kwargs)
#This is the decorator that we'll actually use in real projcts 


def logger(func): 
    def wrapper(*args,**kwargs): 
        print("Start")
        func(*args,**kwargs)
        print("Finished")
    return wrapper


@logger
def greet(name): 
    print(name)

greet("Samir")

#Multiple Argumets. 
@logger
def add(a,b): 
    print(a+b)

add(2,3)

#Key Word Argument : 
@logger
def profile(name, age):

    print(name, age)

profile(name="Sam", age=21)


#Real Backend example : 
def auth(func): 
    def wrapper(*args,**kwargs): 
        print("Checking csrf token . . .")
        func(*args,**kwargs)
    return wrapper

@auth
def dashboard(user): 
    print(f'I PREFER JWT ACCESS TOKEN NOT {user}')

dashboard("csrf")