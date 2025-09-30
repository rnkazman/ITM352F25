# Count the number of strings in a tuple
# Name: Rick Kazman
# Date: 9/30/2025

data = ("hello", 10, "goodbye", 3, "goodnight", 5, "morning", "foobar")
string_count = 0

for my_tuple_item in data:
    if (type(my_tuple_item) == float):  # Check if the item is a string
        string_count += 1
print(f"There are {string_count} floats in the tuple.")
