"""
Name: practise1.py
Purpose: LiveHack2 practise

Author: Ethan Sam
Date: 5/11/2019
"""

# Get values from User
side_one = float(input("Insert first side of triangle: "))

side_two = float(input("Insert second side of triangle: "))

side_three = float(input("Insert third side of triangle: "))

calculation_one = side_one**2 + side_two**2 

calculation_two = side_three**2

# Final Calculation:
if calculation_one == calculation_two:
    print("It is a right angle triangle")
else:
    print("It isn't a right angle triangle")