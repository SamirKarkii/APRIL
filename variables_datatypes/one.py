# 1. Basic Input/Output

# Take a user’s name and age, then print:

# Hello <name>, you are <age> years old.


# name = input("Enter a name ")
# age = int(input("Enter age"))
# if age<=0 or age>105:
#     print("Invalid ")
# else:
#     print(f'Hello {name}, you are {age} years old ')

# Sum of Two Numbers
# Take two integers as input and print their sum.
# a = int(input("Enter number a: "))
# b = int(input("Enter number b:"))
# sum = a+b
# print(sum)

# 3. Swap Two Variables
# Take two numbers and swap them (without using a third variable)
# a =10
# b =a
# print(b)
# b = 20
# a = b
# print(a)

# 4. Type Checking

# Take an input and print its data type.
# a = input(".")
# print(type(a))

# 5. Simple Interest
# Take:
# principal
# rate
# time
# Calculate and print simple interest:
# SI = (P * R * T) / 100
# p =10
# t =1
# r = 10
# si = (p*t*r)/100
# print(si)
# 6. Area of Circle
# Take radius as input and print area.
# 👉 Use:
# π ≈ 3.14
# Formula: πr²
# r = int(input("Enter radius of circle: "))
# π = 3.14
# print(f"The area of circle is {π*r*r}")

# 7. Even or Odd
# Take a number and check whether it is even or odd using operators.
# num = int(input("Enter a number to check whether odd or even"))
# if num%2== 0:
#     print("even")
# else:
#     print("odd")

# 8. Temperature Converter
# Convert Celsius to Fahrenheit.
# Formula:
# F = (C × 9/5) + 32

# c = 10
# F = (c*9/5) + 32
# print(F)

# 9. Quotient and Remainder
# Take two numbers:
# Print quotient
# Print remainder
# 👉 Use // and %

# a = int(input("Entere a number a: "))
# b = int(input("Entere a number b: "))
# quotient = a//b
# print(quotient)
# remainder = a%b 
# print(remainder)

# 10. Expression Evaluation
# Take three numbers a, b, c and print result of:
# a + b * c / (a - b)
# 👉 Watch out for division and precedence
# a = 1
# b = 2
# c =4 
# equation = a + b * c / (a - b)
# print(equation)

# 🚀 Next step (quick challenge)
# Without using tuple swap, fix this:
# a = 5
# b = 9


#core ideal of "third variable" Technique 
#when swapping, the problem is: 
#If you overwrite one variable, you lose its original value 
#so the simple solution is : store one value somewhere safe first 

# a = int(input("Enter a number a: "))
# b = int(input("Enter a number b"))
# temp = a
# a = b 
# b = temp 
# print(a)
# print(b )