import random

# Simple responses database
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just code, but I'm doing great!", "All good here. How about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "what is two plus two": [4],
    "how to declare a variable in python" :["we can declare a python by using this syntax :varname=value"],
    "full form of lpu":["lovely professional university"],
    "what is the procedure to get umc in lpu":["you have to break one thing in side your hostel room or some illegal things"] 
}

def chatbot(user_input):
    # Normalize input
    user_input = user_input.lower()

    # Check for known responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Default response
    return "I don't understand, can you rephrase?"

# Run chatbot
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_text = input("You: ")
    if "bye" in user_text.lower():
        print("Chatbot:", random.choice(responses["bye"]))
        break
    print("Chatbot:", chatbot(user_text))