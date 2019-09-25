"""
Write a program that lets you enter a number of minutes, and that will calculate
the number of days, hours and minutes that represents
"""

print("Welcome to Minutes converter")
minutes = int(input("Please enter time in minutes: "))

print(str(minutes) + " minutes")
print(str(minutes//1440) + " day(s)")
print(str((minutes//1440)//60) + " hour(s)")
print(str(minutes % 1440) + " minute(s)")
