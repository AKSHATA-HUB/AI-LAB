import random
def greet():
    responses = ["Hi there! I'm your friendly chatbot.", 
                 "Hello! How can I assist you today?",
                 "Hey! Welcome to our chat. How can I help you?"]
    return random.choice(responses)
def ask_name():
    responses = ["What's your name?", 
                 "May I know your name?", 
                 "Could you please tell me your name?"]
    return random.choice(responses)
def handle_name(user_input):
    name = user_input.capitalize()
    return f"Nice to meet you, {name}!"
def respond(user_input):
    responses = ["I'm not sure I understand. Can you please clarify?", 
                 "Sorry, I didn't get that. Could you rephrase?", 
                 "Hmm, I didn't catch that. Can you say it differently?"]
    return random.choice(responses)
def chatbot():
    print(greet())
    print(ask_name())
    user_input = input("You: ")
    print(handle_name(user_input))
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Goodbye! Have a great day.")
            break
        else:
            print(respond(user_input))
if __name__ == "__main__":
    chatbot()
