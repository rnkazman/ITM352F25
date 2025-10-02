# Improved quiz game with questions and answers in a dictionary.

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "11", "15", "8"],
    "What is the capital of Texas": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"]
}

for question, answers in QUESTIONS.items():
    correct_answer = answers[0]  # By convention, the first answer in the list is the correct one.
    sorted_answers = sorted(answers)  # Sort answers alphabetically for display.

    for label, answers in enumerate(sorted_answers, start=1):  # Add a number to each possible answer.
        print(f"{label}. {answers}")

    answer_label = int(input(f"{question}? "))  # Get the user's answer as a number.
    user_answer = sorted_answers[answer_label - 1]  # Get the user's answer from the sorted list.

    if user_answer == correct_answer:  # Compare the user's answer to the correct answer.
        print("Correct!")
    else:
        print(f"Incorrect, the answer is {correct_answer!r}, not {user_answer!r}")
