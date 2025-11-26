def get_response(user):
    user = user.lower()

    # greetings
    if "hello" in user or "hi" in user or "hey" in user:
        return "Hello! How can I help you today?"

    # how are you
    elif "how are you" in user:
        return "I'm doing great! Thanks for asking 😊"

    # name
    elif "your name" in user:
        return "I'm a simple Python chatbot created by Rudra!"

    # help
    elif "help" in user:
        return "Sure! Tell me what you need help with."

    # feeling
    elif "sad" in user or "upset" in user:
        return "I'm sorry you're feeling that way. I'm here for you ❤️"

    elif "happy" in user:
        return "That's awesome! Keep smiling 😄"

    # goodbye
    elif "bye" in user or "goodbye" in user:
        return "Goodbye! Take care ✨"

    # fallback
    else:
        return "I'm not sure I understand, but I'm learning!"


def chatbot():
    print("Chatbot: Hello! I'm your Python AI assistant. Type 'bye' to exit.\n")

    while True:
        user = input("You: ")

        response = get_response(user)
        print("Chatbot:", response)

        if "bye" in user.lower():
            break


chatbot()
