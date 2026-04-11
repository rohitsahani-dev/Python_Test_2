import random
import time

def greet():
    responses = ["Hello!", "Hi there!", "Hey! What's up?"]
    return random.choice(responses)

def how_are_you():
    responses = ["I'm fine!", "Doing great!", "All good!"]
    return random.choice(responses)

def get_time():
    return "Current time: " + time.ctime()

def math():
    try:
        expr = input("Bot: Enter an expression: ")
        result = eval(expr)
        return result
    except:
        return "Invalid expression"

def joke():
    return "Why did the Python programmer quit? Because he didn't get arrays."

while True:

    user = input("You: ").lower()

    if "hi" in user or "hello" in user:
        print("Bot:", greet())

    elif "how are you" in user:
        print("Bot:", how_are_you())

    elif "your name" or "what is your name" in user:
        print("Bot: I am your CLI bot.")

    elif "help" in user:
        print("Bot: Try saying hi, ask time, or say bye.")

    elif "time" in user:
        print("Bot:", get_time())

    elif "joke" in user:
        print("Bot:", joke())

    elif "who made you" in user:
        print("Bot: I was made by Rohit Sahani.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    elif "math" in user:
        print("Bot: Let's calculate something.")
        print("Bot:", math())

    else:
        print("Bot: I don't understand. Try 'help'.")