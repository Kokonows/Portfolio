# -*- coding: utf-8 -*-
"""
Created:  January 31, 2020
Author:   Katie Okonowski
Class:    Introduction to Computer Programming
Univ:     Wayne State University
Assign:   Homework 1
"""
# These are user defined functions that will allow players to plug in the 
# variables that they want to perform math functions on.  Each function is 
# named to refer to the type of math that will be performed.  
def addTogether(var1, var2):
    additionTotal = var1 + var2
    return additionTotal

def subtractNumbers(var1, var2):
    subtractionTotal = var2 - var1
    return subtractionTotal

def multiplyTogether(var1, var2):
    multiplicationTotal = var1 * var2
    return multiplicationTotal

def divideNumbers(var1, var2):
    divisionTotal = var1 / var2
    return divisionTotal

# Welcoming to the program.  Setting out instructions with spacing 
# in between lines for best format.  Using the \ to allow for better viewing
# of what's being typed instead of having to scroll to the right.
print("\n") 
print("Welcome to the Amazing Python Calculator!") 
print("---" *15)
print("You will be asked to select two numbers.  You will then be asked which mathematical operation you would like to perform with the two numbers.")
print("\n")
print("The mathematical operations will be addition, subtraction, multiplication, and division.")
print("\n")
print("If you choose subtraction, the first number will be subtracted FROM the second number.")
print("\n")
print("If you choose division, the first number will be divided BY the second number.")
print("\n")
print("Type 'Quit' at any time to quit the game.")
print("\n")
    

# Placing the calculator functions within a "while" loop so that a player can
# choose to continue to play or not after receiving an answer.  The flag that
# is creating the while loop is the answer = "y". The inputs allow a player to
# input the numbers that will be used in the mathematical function of their 
# choosing.
answer = "y"
while answer == "y":

# Asking for the numbers that you want to perform a math function on.
    var1 = input("Please select the first number: ")
    var1 = float(var1)
    var2 = input("Please select the second number: ")
    var2 = float(var2)

# Using the input function to allow players to select the type of math they 
# want to perform on the variables that they have inputted above.
    userSelection = input("What kind of math would you like to perform? \
                          Selections are addition, subtraction, multiplication,\
                          and division: ")
    
# Using if...elif statements to allow the game to navigate to the correct type
# of mathematical operation.  "If...elif" is also used to ask whether the 
# player wants to try again with the math functions, or quit entireley.
# Pass is used if player wants to play again; otherwise, the program stops with
# a good-bye statement and the break function.
    if userSelection == "addition":
            print("\n")
            print("Your result is: " + str(addTogether(var1, var2)))                    
            answer = input("Do you want to try again (y or n): ")
            if answer == ("y"):
                pass
            elif answer == ("n"):
                print("Thank you for playing!")
                break
    elif userSelection == "subtraction":
            print("\n")
            print("Your result is: " + str(subtractNumbers(var1, var2)))
            answer = input("Do you want to try again (y or n): ")
            if answer == ("y"):
                pass
            elif answer == ("n"):
                print("Thank you for playing!")
                break
    elif userSelection == "multiplication":
            print("\n")
            print("Your result is: " + str(multiplyTogether(var1, var2)))
            answer = input("Do you want to try again (y or n): ")
            if answer == ("y"):
                pass
            elif answer == ("n"):
                print("Thank you for playing!")
                break
    elif userSelection == "division":
            print("\n")
            print("Your result is: " + str(divideNumbers(var1, var2)))
            print("\n")
            answer = input("Do you want to try again (y or n): ")
            if answer == ("y"):
                pass
            elif answer == ("n"):
                print("Thank you for playing!")
                break
    elif userSelection == "Quit":
        print("Sorry to see you go. Thanks for playing!")
        break

    