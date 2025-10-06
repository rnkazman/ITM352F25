# First version of quiz game
# Name: Rick Kazman
# Date: 10/2/25

answer = input("What is the airspeed of an unladen swallow in miles/hr? ")
if answer == "12":
    print("Correct!")
else:
    print(f"Incorrect, the answer is '12', not {answer!r}")

answer = input ("What is the capital of Texas? ")
if answer == "Austin":
    print("Correct!")
else:
    print(f"Incorrect, the answer is 'Austin', not {answer!r}")