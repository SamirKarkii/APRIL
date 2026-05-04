# #In python break, continue, and pass are control flow statement used to alter the execution flow of loop (for and while ) and other structure 

# #Break 
# #the break statement terminates the entire looop immediately . Once the code encounters a break, the loop stops, and the program control 
# #the progream control moves to the first statement following the looo 

# #when to use it: Use this when you have found what you were looking for a specific condition is met, and ther is no 
# #reason to continue checking the remaining iteratioons 

# # for i in range(1,10):
# #     if i== 5: 
# #         break #loop stops completely when number is 5 
# #     print(i)

# # for i in range(1,100):
# #     if i ==10:
# #         break
# #     print(i)

# "Continue"
# #the continue statement skips the remainder of the current iteration and jumps back to the top of the loop to begin the 
# #next iteration 
# #when to use: use this when you want to bypass specific data pints or conditions without stopping entite loop.

# # for i in range(1,10):
# #     if i%2==0: 
# #         continue
# #     print(i)

# #pass : the pass statement is a null operation. It literally does nothing. When pytho executes pass, it continues to the next
# #line of conde. 

# secret_number = 10
# count = 0
# user = int(input("Guess the correct number:"))

# while user!=secret_number: 
#     if user>secret_number:
#         print("The number is too high")
#         user = int(input("Guess the correct number:"))
#     else:
#         print("The number is too low ")
#         user = int(input("Guess the correct number:"))
#     count = count + 1

# count = count+1
# print(f'you guess it {count} time')



# secret_number = 10
# count = 0

# while True:
#     user = int(input("Guess the correct number: "))
#     count += 1
#     if user == secret_number:
#         print("You guessed it!")
#         break
#     elif user > secret_number:
#         print("Too high")
#     else:
#         print("Too low")

# print(f"You guessed it in {count} attempts")