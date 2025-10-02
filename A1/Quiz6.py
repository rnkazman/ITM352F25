# Improved quiz game with questions and answers in a dictionary.
# Iterate until the user enters a correct alternative.
# Keep track of correct answers.
# Randomize the questions and possible answers
# Name: Rick Kazman
# Date: 10/2/25

from string import ascii_letters
import random

NUM_QUESTIONS_PER_QUIZ = 5

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "11", "15", "8"],
    "What is the capital of Texas": ["Austin", "Dallas", "Houston", "San Antonio"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "What is the smallest prime number": ["2", "1", "3", "7"],
    "What is the largest planet in our solar system": ["Jupiter", "Saturn", "Earth", "Neptune"]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
selected_questions = random.sample(list(QUESTIONS.items()), num_questions)
num_correct = 0

for qnum, (question, answers) in enumerate(selected_questions, start=1):
    print(f"Question {qnum}:")
    print(f"{question}? ")
    correct_answer = answers[0]  # By convention, the first answer in the list is the correct one.
    labelled_answers = dict(zip(ascii_letters, random.sample(answers, k=len(answers))))  # Create a dictionary of labelled answers.

    for label, answer in labelled_answers.items():  # Add a letter to each possible answer.
        print(f"{label}. {answer}")

    while (answer_label := input(f"\nChoice? ")) not in labelled_answers:
        print(f"Invalid choice. Please enter one of {', '.join(labelled_answers)}")

    answer = labelled_answers[answer_label]  # Get the user's answer from the labelled list.

    if answer == correct_answer:  # Compare the user's answer to the correct answer.
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} out of {len(QUESTIONS)} questions correct.")