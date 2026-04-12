import random
import time

mood = "professional"  

def greet(mood):
    if mood == "professional":
        responses = ["Hello!", "Hi there!", "Hey! What's up?"]
    else:
        responses = ["What's up bro?", "Hi brother!", "Hey! What's up, dude?"]
    return random.choice(responses)

def how_are_you(mood):
    if mood == "professional":
        responses = ["I'm fine!", "Doing great!", "All good!"]
    else:
        responses = ["I'm fine, bro!", "Great, brother!", "All perfect, yo!"]
    return random.choice(responses)

def get_time(mood):
    time_str = "Current time: " + time.ctime()
    if mood == "professional":
        return time_str
    else:
        return time_str + " dude"

def joke(mood):
    if mood == "professional":
        return "Why did the Python programmer quit? Because he didn't get arrays."
    else:
        return " Why was the Python list excited? It had a lot of friends appended." 

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"
    
while True:
    user = input("You: ").lower()

    if "casual" in user:
        mood = "casual"
        print("Bot: Switched to casual mode! 😎")

    elif "professional" in user:
        mood = "professional"
        print("Bot: Switched to professional mode. 🧑‍💼")

    elif "hi" in user or "hello" in user:
        print("Bot:", greet(mood))

    elif "how are you" in user:
        print("Bot:", how_are_you(mood))

    elif "your name" in user or "what is your name" in user:
        print("Bot: I am your CLI bot.")

    elif "help" in user:
        print("Bot: Try saying 'hi', 'time', 'joke', 'math', 'casual', 'professional', or 'bye'.")

    elif "time" in user:
        print("Bot:", get_time(mood))

    elif "joke" in user:
        print("Bot:", joke(mood))

    elif "who made you" in user:
        print("Bot: I was made by Rohit Sahani.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    elif "calculate" in user or "math" in user:
        while True:
            try:
                a = float(input("Enter first number: "))
                op = input("Enter operator: ")
                if op not in ["+", "-", "*", "/"]:
                    print("Invalid input")
                    continue

                b = float(input("Enter second number: "))

                result = calculate(a, b, op)
                print("Result:", result)

            except ValueError:
                print("Enter only number.")
            except:
                print("Something went wrong.")

            cont = input("Continue? (yes/no): ").lower()
            if cont != "yes":
                break
    else:
        print("Bot: I don't understand. Try 'help'.")   



