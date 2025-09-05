# Ask the user to enter their weight in pounds.  Convert this to
# kilograms and return the value to the user.
# Name: Rick Kazman
# Date: 9/5/25

weight_in_pounds = input("Please enter your weight in pounds: ")
weight_in_kilos = float(weight_in_pounds) * 0.45359237
weight_in_kilos_rounded = round(weight_in_kilos)
print(f"You weigh  {weight_in_kilos_rounded} kilograms.")
