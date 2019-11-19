"""
Name: LiveHack2.py
Purpose: Determining if the current shape is a triangle

Author: Ethan Sam
Date: 19/11/19
"""

# Get side angles from user
side_One = float(input("Input first angle: "))
side_Two = float(input("Input second angle: "))
side_Three = float(input("Input third angle: "))

# Determining if it is a triangle
print("Welcome to TriangleChecker2019!")
if side_One == side_Two == side_Three and side_One + side_Two + side_Three == 180:
    print("It is an equilateral triangle")
elif side_One == side_Two and side_One + side_Two + side_Three == 180:
    print("It is an isosceles triangle")
elif side_One == side_Three and side_One + side_Two + side_Three == 180:
    print("It is an isosceles triangle")
elif side_Two == side_Three and side_One + side_Two + side_Three == 180:
    print("It is an isoceles triangle")
elif side_One != side_Two != side_Three and side_One + side_Two + side_Three == 180:
    print("It is a scalene triangle")
else:
    print("Error, the angles do not form a triangle")