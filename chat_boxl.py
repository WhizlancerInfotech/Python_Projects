import random
import spacy

nlp = spacy.load("en_core_web_sm")

responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm good, how about you?", "Doing great!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def chatbot_response(user_input):
    doc = nlp(user_input.lower())
    for key in responses.keys():
        if key in doc.text:
            return random.choice(responses[key])
    return "Sorry, I don't understand."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
