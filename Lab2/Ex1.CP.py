# Prompt the user to enter a whole number between 1 and 100, with input validation
while True:
	num_str = input("Enter a whole number between 1 and 100: ")
	try:
		num = int(num_str)
		if 1 <= num <= 100:
			break
		else:
			print("Please enter a number between 1 and 100.")
	except ValueError:
		print("Invalid input. Please enter a whole number.")
square = num ** 2
print(f"You entered {num}. The square of {num} is {square}.")
