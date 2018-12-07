################
# Project Name: Basic Calculator
# Project Description: Basic calculator created in Python. This calculator can add, subtract, multiply, and divide well also getting the remainder of a division problem.
# Project By: Brian Leek
# Last Edited: 12/7/18
################

# Sets up a function for addition.
def addition(x, y):
    return x + y

# Sets up a function for subtraction.
def subtraction(x, y):
    return x - y

# Sets up a function for multiplication.
def multiplication(x, y):
    return x * y

# Sets up a function for division.
def division(x, y):
    return x / y

# Gives the user options and let them pick one.
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")
option = input("Please pick a option: ")

# Let the user input the numbers they want.
number1 = int(input("Please enter your first number: "))
number2 = int(input("Please enter your second number: "))

# Gets the remainder of the two numbers.
remainder = number1 % number2

# Addition.
if option == '1':
    print(number1,"+",number2,"=",addition(number1, number2))
# Subtraction.
elif option == '2':
    print(number1,"-",number2,"=",subtraction(number1, number2))
# Multiplication.
elif option == '3':
    print(number1,"x",number2,"=",multiplication(number1, number2))
# Division.
elif (option == '4'):
    print(number1,"÷",number2,"=",division(number1, number2))
    # If remainder is 0 do nothing.
    if remainder == 0:
        pass
    # If remainder is greater than 0 print it out.
    else:
        print("with a remainder of",remainder)
# Gives the user a error if they do something wrong.
else:
    print("Something went wrong. Please try again.")
