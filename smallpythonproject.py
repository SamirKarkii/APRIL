#Making a simple Calculator using python 

# Simple Calculator in Python

def add(a,b):
    return a+b

def sub(a,b): 
    return a-b

def mul(a,b): 
    return a*b

def divide(a,b): 
    if b==0: 
        return "Error! Division by Zero "
    return a/b

print("Simple Pythonic Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")

choice = input("Enter a choice(1/2/3/4): ")
num1 = int(input("Enter the first number mate: "))
num2 = int(input("Enter the first number mate: "))

if choice== '1': 
    print("Result",add(num1,num2))
elif choice == '2': 
    print("Result", sub(num1,num2))
elif choice == '3': 
    print("Result", mul(3,4))

elif choice == '4': 
    print("Result", divide(3,4))

else: 
    print("Heck!What's wrong with you input mate ")


#Basic number guessing : 
from random import randint

computer = randint(1,100)
count = 0

while True: 
    user = int(input("Give it a guess: "))
    count = count+1

    if user == computer: 
        print