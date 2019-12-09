"""
Name: practise2.py
Purpose: LiveHack 2 practice

Author: Ethan Sam
Date: 5/11/2019
"""
# Get mark and money from student
mark = float(input("Insert Mark Here: "))

money = float(input("Insert amount earned: "))

# if statement and final calculation
if mark >= 80.0 and money >= 500:
    print("You can go to Europe! ")
elif mark >= 80.0 and money < 500:
    print("You can go to California! ")
else:
    print("Sorry, you can't go anywhere")