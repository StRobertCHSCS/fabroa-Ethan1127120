"""
Name: problem2.py
Purpose: Detect amount that Uber driver drives

Author: Ethan Sam
Date: 9/12/19
"""
# Welcome Statement
print(" ***** Welcome to the Distance Tracker ****** ")

# Set values
days = 0
distance = 0

# While loop in order to get amount of days
while distance < 100:
    addition = int(input("Enter the distance travelled for the day: "))
    days += 1
    distance += addition

# Final Statement
print("It took " + str(days) + " days to surpass 100km driven.")
print("The average distance driven per day is " + str(distance/days) + "km")