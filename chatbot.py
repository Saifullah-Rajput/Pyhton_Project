import random

# Define simple responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm fine, thank you!", "Doing great! What about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase that?", "I'm not sure I get what you mean."]
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Run chatbot loop
print("Bot: Hi! I'm your chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Bot:", random.choice(responses["bye"]))
        break
    response = get_response(user_input)
    print("Bot:", response)
