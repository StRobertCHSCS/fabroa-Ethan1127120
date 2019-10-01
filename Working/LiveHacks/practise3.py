"""
Name: practise3.py
Purpose: Calculate minutes to days, hours, and leftover minutes

Author: Ethan Sam
Date: Wed, Sept 25, 2019

Write a program that lets you enter a number of minutes, and that will
calculate the number of days, hours and minutes that represents
"""
# Welcome
print("Welcome to Minutes converter")

# Input minutes
minutes = int(input("Please enter time in minutes: "))

# Calculate for days
days = minutes//1440

# Calculate for hours
hours = (minutes//60) % 24

# Calculate for minutes
minute = (minutes % 60)

# Final Calculation
print("Entered number of minute(s): " + str(minutes))
print(str(days) + " day(s)")
print(str(hours) + " hour(s)")
print(str(minute) + " minute(s)")
