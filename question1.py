#Question 1

"""
1. Write a small program that assigns an angle in degrees to a variable called degrees. The program converts
this angle to radians and assigns it to a variable called radians. To convert from degrees to radians, use the
formula radians = degrees * 3.14 / 180 (where we are using 3:14 to approximate pi). Print the angle in both
degrees and radians.
The following demonstrates the program output when the angle is 150 degrees:
Degrees: 150
Radians: 2.616666666666667
"""

degrees = input("Degrees: ")
radians = float(degrees) * 3.14 / 180.0
print("Radians:", radians) 