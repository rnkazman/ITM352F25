# Ask the user to enter a number between 1 and 100.  Square the number
# and print the result.
# Name: Rick Kazman
# Date: 9/3/25

print("Hi there")
value_entered = input("Please enter an integer between 1 and 100: ")
print("The user entered ", value_entered)
value_as_integer = int(value_entered)

value_squared = value_as_integer**2
print(f"The value squared is {value_squared}")
