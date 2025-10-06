# Quiz 2: put questions/answers into a list of tuples
# Name: Rick Kazman
# Date: 10/2/25

QUESTIONS = [
    ("What is the airspeed of an unladen swallow in miles/hr", "12"),
    ("What is the capital of Texas", "Austin"),
    ("The Last Supper was painted by which artist", "Da Vinci")
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect, the answer is {correct_answer!r}, not {answer!r}")