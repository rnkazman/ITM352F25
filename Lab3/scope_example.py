# This program demonstrates how scope works in Python

# discount = 0.6

def calculate_discount(price):
    # This is a local variable in the calculate_discount function
    # After applying the 10% discount increase it to 20%
    discount = 0.9
    price = price * discount
    print(f"Discounted price inside the function: ${price:.2f}")
    discount = 0.8  
    return price

# Global scope
# This is a global variable
price = 100.0  # Total price of an item

print(f"Original price in the main program: ${price:.2f}")

# Call the function to calculate the discounted price
discounted_price = calculate_discount(price)

print(f"Price after discount in the main program: ${discounted_price:.2f}")
print("Discount = ", discount)