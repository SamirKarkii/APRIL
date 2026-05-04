# 1. Positive, Negative, or Zero

# Take a number and print:

# “Positive”
# “Negative”
# “Zero”

# a = int(input("Enter a number to whether it is positve , negative or zero: "))
# if a>0:
#     print(f'{a} is a positive number')
# elif a==0:
#     print(f'the value is {a}')
# else:
#     print(f'{a} is a negative number ')

# 2. Even, Odd, or Zero
# Extend your previous logic:
# If number = 0 → print “Zero”
# Else check even/odd
# a = int(input("Enter a number to know whether its even , odd , zero: "))
# if a == 0:
#     print("The number is 0")
# elif a%2==0:
#     print("The number is even ")
# else:
#     print("The number is odd ")

# 3. Largest of Three Numbers
# Take 3 inputs and print the largest.
# ⚠️ Don’t use max().
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# c = int(input("Enter a number:"))
# if a>b and a >c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# 4. Simple Calculator
# Take:
# two numbers
# one operator (+, -, *, /)
# Perform operation using if-elif

# a = int(input("Enter a number a: "))
# b = int(input("Enter a number b: "))
# operation = input("Enter an operator")
# if operation== '+':
#     print(a+b)
# elif operation == '-':
#     print(a-b)
# elif operation == '*':
#     print(a*b)
# else :
#     operation== "/"
#     print(a/b)
    
# 🔁 Phase 2: Loops Basics
# 5. Print Numbers (for loop)
# Print numbers from 1 to N
# N = 5 
# for i in range(1,N+1):
#     print(i)

# 6. Sum of N Numbers
# Take N → print sum from 1 to N
# n = int(input("Enter a number n: "))
# total  = 0
# for i in range(1, n+1):
#     total = total +i 
# print(total)


#   👉 Q7: Multiplication Table
# Example:
# Input: 5  
# Output:
# 5 x 1 = 5  
# 5 x 2 = 10  
# ...
# 5 x 10 = 50
# n = int(input("Enter a number to get its multiplication table: "))
# for i in range(1,11):
#     print(f'{n}*{i}= {n*i}')


# 👉 Q8: Count Digits (IMPORTANT 🔥)
# Example:
# Input: 12345  
# Output: 5
# 👉 Use while loop, not for


# n = 12345 
# count = 0

# while n>0:
#     n = n//10
#     count = count+1  
# print(count)

#wap to reverse a number 


#write a python program where: 
#the program has a secret number (for now, hardcoded it, e.g , 10)
#the user keeps guessing the number 
#the program gives feedback after each guess 
# user = 10
# count = 0 
# user = int(input("Enter a guess: "))
# while user>10 and user<10:
#     print("wrong guess")
#     user = int(input("Enter a guess"))
#     count = count+1 
# print("you guess it correct ")
# print(f'It took you {count} attempts ')

# count = 0 
# user = int(input("Enter a guess: "))
# while user == 10:
#     print("you guessed it correst")
#     if user>10:
#      print("you guessed it too high")
#      user = int(input("Enter a guess: "))
#      count = count+1 

#     elif user<10:
#        print("You guessed it too low ")
#        user = int(input("Enter a guess: "))
#        count = count+1 

# print(f'IN {count} time you guessed it correctly')

#while user ==10:
#meaning loop only runs when already correct , but we want the loop to keep going until it becomes correct 
#when should loop continue?
#when the answer is incorrect the loop should continue else it should stop 

