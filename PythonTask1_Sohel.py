
#--Task 1:- CALCULATOR

# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
#____________________________________________________________________
import math


# Function to perform addition
def add(x, y):
    return x + y


# Function to perform subtraction
def subtract(x, y):
    return x - y


# Function to perform multiplication
def multiply(x, y):
    return x * y


# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Function to perform exponentiation
def exponentiate(x, y):
    return x ** y


# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Cannot calculate square root of a negative number"
    return math.sqrt(x)


# Function to calculate modulus
def modulus(x, y):
    if y == 0:
        return "Cannot calculate modulus with zero divisor"
    return x % y


# Main program
while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'ex' for exponentiation")
    print("Enter 'sq' for square root")
    print("Enter 'mod' for modulus")
    print("Enter 'quit' to end the program")

    user_choice = input("Enter operation: ").lower()

    if user_choice == "quit":
        break

    if user_choice in ("+", "-", "*", "/", "ex", "sq", "mod"):
        if user_choice in ("sq", "mod"):
            num1 = float(input("Enter a number: "))
            if user_choice == "sq":
                print("Result:", square_root(num1))
            else:
                num2 = float(input("Enter divisor: "))
                print("Result:", modulus(num1, num2))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_choice == "+":
                print("Result:", add(num1, num2))
            elif user_choice == "-":
                print("Result:", subtract(num1, num2))
            elif user_choice == "*":
                print("Result:", multiply(num1, num2))
            elif user_choice == "/":
                print("Result:", divide(num1, num2))
            elif user_choice == "ex":
                print("Result:", exponentiate(num1, num2))
    else:
        print("Invalid input. Please enter a valid operation.")
