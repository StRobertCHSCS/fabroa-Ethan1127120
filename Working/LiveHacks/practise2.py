"""
Name: practise2.py
Purpose: Converts hours to days and hours

Name: Ethan Sam
Date: Wed, Sept 25, 2019

Write a program that lets you enter a number of hours, and that converts it to
days and hours. For example, 111 hours = 4 days and 15 hours.
"""

# Welcome
print("Welcome to Hours to days converter!")
time = int(input("Please enter time in hours: "))

# Dependant Variables
days = time//24
hours = time % 24

# Final Statement
print(str(days) + " days and " + str(hours) + " hours")
