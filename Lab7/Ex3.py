#data = ("hello", 10, "goodbye", 3, "goodnight", "Morning")
data = ()
string_count = 0

for item in data:
    if type(item) == str:
        string_count += 1
print(f"There are {string_count} strings in the data tuple.")
