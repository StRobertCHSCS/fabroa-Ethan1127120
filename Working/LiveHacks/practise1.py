"""
Name: Practise1.py
Purpose: Calculate Fahrenheit to Celcius

Author: Ethan Sam

Date: Wed, Sept 25, 2019

Write a program that lets you enter a degree measure in Fahrenheit,
and that prints the result in celsius degree measure
"""

# Welcome sign
print("Welcome to Fahrenheit to Celcius converter!")

# Get input fahrenheit
fahrenheit = int(input("Enter Fahrenheit: "))

# Converts to celcius
print("Celcius: " + str(5/9*(fahrenheit-32)))
