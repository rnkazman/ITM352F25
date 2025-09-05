# Ask the user to enter a floating point (decimal) number between 1 and 100.  Square the number
# and print the result.
# Name: Rick Kazman
# Date: 9/3/25

value_entered = input("Please enter an floating point number between 1 and 100: ")
print("The user entered ", value_entered)
value_as_float = float(value_entered)

value_squared = value_as_float**2
print(f"The value squared is {value_squared}")
