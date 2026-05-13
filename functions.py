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

def profile(name,country="Nepal"):
    print("Name:", name)
    print("Country:",country)

profile("Sam")
profile("sam", "georgia") #ohh it even overrides great 