# Ask the user to enter a temperature in degrees Fahrenheit.
# Convert this to degrees Celsius and return the value to the user.
# Name: Rick Kazman
# Date: 9/5/25
degreesF = input("Enter a temperature in degrees Fahrenheit: ")

degreesF_float = float(degreesF)
degreesC = (degreesF_float - 32) * 5.0/9.0
degreesC = round(degreesC,1)

print(f"{degreesF_float} degrees Fahrenheit is {degreesC} degrees Celsius.")
