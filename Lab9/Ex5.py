# Save the dictionary of quiz questions as a JSON file
import json

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr": ["12", "13", "24", "36", "48"],
    "What is the capital of Texas": ["Austin", "Dallas", "Houston", "Waco"],
    "The Last Supper was painted by which artist": ["Da Vinci", "Michelangelo", "Raphael", "Donatello"],
    "Which class novel opens with the line 'Call Me Ishmael'": ["Moby Dick", "The Great Gatsby", "1984", "To Kill a Mockingbird"]
}

JSON_file = "quiz.json"

# Open the file in write mode and save the QUESTIONS dictionary as JSON
with open(JSON_file, "w") as json_file:
    json.dump(QUESTIONS, json_file, indent=4)

print(f"Quiz questions saved to {JSON_file}")
