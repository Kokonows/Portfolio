# -*- coding: utf-8 -*-
"""
Date: April 15, 2020 (the Quarantimes)
Assignment: Group Assignment - Plane Tickets 
Authors: Katie Okonowski, Soumaya Al-Ahmedi, Andy Marcum
Class: INF 6050 - Intro to Computer Programming.

"""
import pprint
import random
pp = pprint.PrettyPrinter(indent=4)

DEMOGRAPHICS = ('Name', 'Age') # Customer information

CLASSES = ('Business', 'Economy', 'First') # Class listing

OPTIONS = {
    "Business":
        {
            "Meal": 
                ["Chicken", "Veggie"],
            "Beverage":
                ["Soda", "Coffee", "Tea"]
        },
    "Economy":
        {
            "Meal": 
                ["Hotpocket", "Pretzels"],
            "Beverage":
                ["Water"]
        },  
    "First":
        {
            "Meal": 
                ["Steak", "Lobster", "Linguini"],
            "Beverage":
                ["Beer", "Wine", "Fruit Juice"]
        }       
}

firstClassSeats = ("1A", "2B", "3C", "4D", "4E", "4F", "2A", "2B", "2C", "2D", "2E", "2F", "3A", "3B", "3C", "3D", "3E", "3F")
businessClassSeats = ("4A", "4B", "4C", "4D", "4E", "4F", "5A", "5B", "5C", "5D", "5E", "5F", "6A", "6B", "6C", "6D", "6E", "6F")
economyClassSeats = ("7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C", "8D", "8E", "8F", "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E", "10F")

# User Defined functions

# Welcome message        
def welcomeMessage():
    pp.pprint("Thanks for joining S-K-A airlines! We are happy to serve you.")
    print("\n") 
    pp.pprint("You are going to be asked a series of questions for security and reservations.")
    print("\n") 
    pp.pprint("We hope you enjoy your flight!")
    print("\n") 
    pp.pprint("If you need to leave your selection, please type 'quit' at any time!")

# End message
def quitMessage():
    pp.pprint("Thank you for choosing to fly S-K-A airlines!")
    print("\n")
    pp.pprint("We hope you enjoy your time with us and look forward to serving you further!")
    print("\n")
    
# Check for Quit function that can be used in other functions.
    
def checkForQuit(x):     
    """
    Check for the string 'QUIT'
    """
    if isinstance(x, str):   
        if x.upper() == 'QUIT': # .upper to ensure you can do upper and lowercase.
            return True
        else:
            return False
    else:
        return False
    

# Grabbing passenger information.
        
def getPassengerInfo(d): 

    """
    # Grab User Passenger information

    d = demographic info to collect
    
    """
    checkForQuit(d)
    passengers = list() # Sets up for list to contain/store.
        
    for i in range(0, 1): # Asking for current passenger
        
        print("\n"* 5) 

        temp = dict() # Sets up temporary dictionary
        checkForQuit(d)
        for ask in d: # d variable stands for demographic info to collect.

            # Age is an integer, so will perform a validation check..
            # outer if..else shell; inner while loop with if/try/except.
            if ask == "Age":
                
                while True:
                    a = input("Please provide the " + ask + " of the ticket holder : ") 
                    
                    # Passengers can quit at any time
                    if checkForQuit(a):
                        return False # break out of function and return False

                    try:
                        a = int(a) # Placeholder
                        temp[ask] = a  
                        break
                    except:
                        print("Please enter a numeric value.")

            # everything else is a string
            else:
                a = input("Please provide the " + ask + " of the ticket holder : ")
                
                # Check for Quit
                
                if checkForQuit(a):
                    return False # break out of function and return False

                temp[ask] = a # Allows for temporary asking to be stored in variable 'a'.

        passengers.append(temp) # Temporarily appends to the  passengers = list() that we set up previously in the function.
    
        return passengers


# Defining the beverage and meals you will receive based on the class you select.
def getBevMeals(CLASSES):
    
    """
    Asking the player for what class they chose
    Then telling them the option for meals and beverage based on class
    """
    
    print("\n"*3)    
    print("Pick the numeric value associated with the class you've selected based on below:")
    print("\n")

    for key, a_class in enumerate(CLASSES):
        print("\t - " + a_class + " -- type " + str(key))
        
    print("\n")
    
    userChoice = int(input("What is your class (enter the number corresponding to the class): "))
    
    userChoiceValue = CLASSES[userChoice]
    mealOptions = OPTIONS[userChoiceValue]["Meal"]
    beverageOptions = OPTIONS[userChoiceValue]["Beverage"]
    
    print("Your meal options are : " + str(mealOptions) + ", and you may be served: " + str(beverageOptions) + " .")
    

# Using the random.choice option to select the seat for the person and assign price
    
def seatRow():
    """
    Picking the seat assignment based on user selection of class
    Asking for user input for external data
    """

    print("\n"*3)
        
    userSeat = input("What class are you choosing, First, Business, or Economy? : ")
    # Check for Quit
    checkForQuit(userSeat)
    # if/elif to choose class seats
    if userSeat == "First":
        random.choice(firstClassSeats)
        print("Your seat number is : " + firstClassSeats.pop(random.choice(firstClassSeats)))
        print("Your total will be $ 1500.")

    elif userSeat == "Business":
        random.choice(businessClassSeats)
        print("Your seat number is : " + businessClassSeats.pop(random.choice(businessClassSeats)))
        print("Your total will be $1200.")

    elif userSeat == "Economy":
        random.choice(economyClassSeats)
        print("Your seat number is : " + economyClassSeats.pop(random.choice(economyClassSeats)))
        print("Your total will be $1000.")

    return seatRow

"""
Start of running program
"""
# Execute user defined functions
welcomeMessage()

anotherTicketQuestion = "y"
while anotherTicketQuestion == "y":
    
    getPassengerInfo(DEMOGRAPHICS)
    print("\n")
    seatRow()
    getBevMeals(CLASSES)
    
    anotherTicketQuestion = input("Do you need to ask for another ticket (y or n): ")
    if anotherTicketQuestion == ("y"):
        continue
    elif anotherTicketQuestion == ("n"):
        print("\n")
        break
quitMessage()


