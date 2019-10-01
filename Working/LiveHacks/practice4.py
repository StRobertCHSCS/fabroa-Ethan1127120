"""
Name: practise4.py
Purpose: Calculates temperature and windspeed as independant variables
then calculates the windchill factor as a dependant variable

Author: Ethan Sam
Date: Thurs, Sept 26, 2019

Write a program that gets the temperature(celsius)
and wind speed (km/h) then computes and outputs  the windchill factor.
"""
# Input Statements
temperature = int(input("Enter the temperature in celcius: "))
windspeed = int(input("Enter the windspeed (km/hr): "))

# Part 1

# Final Calculation
print("Wind chill factor: " + str(13.12+(.6125*temperature)-(
    11.37*windspeed**0.16)+(.3965*temperature*windspeed**0.16)))
