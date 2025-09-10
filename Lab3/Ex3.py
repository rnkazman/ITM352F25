def square_root(x, precision=2):
    if x < 0:
        raise ValueError("Error: Cannot compute square root of a negative number.")
    return round(x ** 0.5, precision)

number = float(input("Enter a number: "))
result = square_root(number)
print(f"The square root of {number} is {result}")
