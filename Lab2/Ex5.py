# Ask the user to enter an arbitrary sentence.  Calculate the length of
# the sentence and return the length to the user.
# Name: Rick Kazman
# Date: 9/5/25

user_sentence = input("Please enter a sentence: ")

sentence_length = len(user_sentence)
print("You entered:", user_sentence)
print(f"The length of the sentence is: {sentence_length}")