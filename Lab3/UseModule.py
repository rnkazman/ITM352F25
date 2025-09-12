# Test to see how the functions defined in HandyMath work.
# Name: Rick Kazman
# Date: Sept. 12, 2025

#import HandyMath as HM
from HandyMath import max, min

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

mid = HandyMath.midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {mid}")

exp = HandyMath.exponent(number1, number2)
print(f"{number1} raised to the power of {number2} is {exp}")

max_number = HandyMath.max(number1, number2)
print(f"The maximum of {number1} and {number2} is {max_number}")

min_number = HandyMath.min(number1, number2)
print(f"The minimum of {number1} and {number2} is {min_number}")

sq_root = HandyMath.square_root(number1) 
print(f"The square root of {number1} is {sq_root}")