import datetime
import random

print("=" * 50)
print("Welcome to DecodeBot AI")
print("Type 'help' to see commands")
print("Type 'bye' to exit")
print("=" * 50)

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it forgot to close Windows!",
    "Why do Python developers wear glasses? Because they can't C.",
    "Why did the AI go to school? To improve its neural network!"
]

while True:

    try:

        user = input("\nYou: ").strip().lower()

        if user == "":
            print("Bot: Please type something.")
            continue

        elif user in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you")

        elif user == "how are you":
            print("Bot: I am doing great!")

        elif user in ["your name", "who are you"]:
            print("Bot: I am DecodeBot AI Assistant")

        elif user == "time":
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Bot: Current time is {current_time}")

        elif user == "date":
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {current_date}")

        elif user == "joke":
            print("Bot:", random.choice(jokes))

        elif user == "help":
            print("\nAvailable Commands:")
            print("hello / hi")
            print("how are you")
            print("your name")
            print("time")
            print("date")
            print("joke")
            print("calculate")
            print("bye")

        elif user == "calculate":

            expression = input("Enter calculation: ")

            try:
                result = eval(expression)
                print(f"Bot: Result = {result}")

            except:
                print("Bot: Invalid expression")

        elif user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that")

    except KeyboardInterrupt:
        print("\nBot: Program closed safely")
        break

    except Exception as e:
        print("Bot: Error occurred")
        print("Error:", e)