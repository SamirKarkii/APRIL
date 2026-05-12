#Error happen, Whether its a user enterig a string where anumber should be or a severgoing offilnie, you code needs a way to handle these
#'exception' without crashing. IN python we use tyr .. except block to manage these momemts grace fully

#the basics Structure 
#Think of try block as a safety net. YOu put the "risky" code inside the try section, if something goes wrong, Python jumps to except section instead
#of stopping the program 

try:
    number = int(input("Enter a divisor:"))
    result = 10/number
    print(f"Result{result}")
except:
    print("oops")