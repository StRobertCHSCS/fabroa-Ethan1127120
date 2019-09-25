"""
Write a program that lets you enter a number of hours, and that converts it to
days and hours. For example, 111 hours = 4 days and 15 hours.
"""
print("Welcome to Hours to days converter!")
time = int(input("Please enter time in hours: "))

print(str(time) + " hours:")
print(str(time//24) + " days and " + str(time % 24) + "hours")
