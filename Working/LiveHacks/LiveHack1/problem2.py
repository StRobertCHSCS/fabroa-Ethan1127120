"""
Name: problem2.py
Purpose: Evenly distribute Popeyes Chicken and remainder goes to Mr. Fabroa

Author: Ethan Sam
Date: 02/10/2019
"""

# Get inupt of the number of students
students = int(input("Enter the number of students in Mr. Fabroa's class: "))

# Get input of the amount of chicken won
chicken = int(input("Enter amount of chicken won: "))

# Get evenly distributed chicken:
remainder = chicken//students

# Final Calculation
print("Each student gets " + str(remainder) + " amount of chicken and Mr. Fabroa gets " + str(chicken % remainder))
