"""
Name: Problem1.py
Purpose: Keeping track of heating days

Author: Ethan Sam
Date: 9/12/19
"""
# Welcome Statement
print("******  Heating Days Tracker ******")

# Get track number of days
heat_days = int(input("Enter the number of days to track: "))

# Set amount of heat days
days = 0

# Repeating statement to get heat days
for i in range(1,heat_days + 1):
    temperature = int(input())
    if temperature < 15:
        days += 1

print("There are " + str(days) + " heating days.")