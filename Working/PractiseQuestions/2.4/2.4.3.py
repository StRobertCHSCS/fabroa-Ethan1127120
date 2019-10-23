"""
Name: 2.4.3.py
Purpose: Logical operators practice

Author: Ethan Sam
Date: 22/10/2019
"""
# Talking Parrot!
confirm = "y"
parrot_Talking = str(input("Is the parrot talking? (y/n): "))
yes_Talking = confirm == parrot_Talking

# Input Hour
hour = int(input("What is the hour?: "))

# Final Statement
if yes_Talking and hour < 7:
    print("We are in trouble!")
elif yes_Talking and hour > 20:
    print("We are in trouble!")
else:
    print("Everything is fine.")