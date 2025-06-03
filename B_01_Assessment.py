import random

def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes / no")

def instructions():
    print('''
    In this game, you will be asked math questions.
    You can choose how many rounds you want and a difficulty level (1–5).
    Try to get as many correct answers as possible.
    Good luck!
    ''')

def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer."
    elif low is not None and high is None:
        error = f"Please enter an integer >= {low}"
    else:
        error = f"Please enter an integer between {low} and {high}"

    while True:
        response = input(question)
        if response == exit_code:
            return response
        try:
            response = int(response)
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

def generate_level(level):
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-'])

    elif level == 2:
        num1 = random.randint(10, 25)
        num2 = random.randint(10, 25)
        operator = random.choice(['+', '-'])

    elif level == 3:
        num1 = random.randint(25, 50)
        num2 = random.randint(25, 50)
        operator = random.choice(['+', '-', '*'])

    elif level == 4:
        num1: int = random.randint(50, 100)
        num2: int = random.randint(50, 100)
        operator: int = random.choice(['+', '-', '*'])

    elif level == 5:
        num1: int = random.randint(100, 200)
        num2: int = random.randint(100, 200)
        operator: int = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = round(num1 / num2)

    return num1, operator, num2, answer

# Welcome the user
print("Welcome to Quiz quest.")

# ask the user if they want to see the instructions
want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# ask the user if they want the default number of rounds / how many rounds
default_rounds = yes_no("Do you want to use the default number of rounds? ")
if default_rounds == "yes":
    num_rounds = 10
else:
    num_rounds = int_check("How many rounds would you like? ", 1)

print(f"\nThere will be {num_rounds} rounds.")

# ask user to choose level 1-5
level = int_check("Choose a level (1-5): ", 1, 5)
print(f"\nYou chose Level {level}.")

game_history = []
rounds_played = 0
score = 0

# ask user the question
while rounds_played < num_rounds:
    print(f"\nRound {rounds_played + 1} of {num_rounds}")
    num1, operator, num2, answer = generate_level(level)
    print(f"\nWhat is {num1} {operator} {num2}?")

    try:
        user_answer = int_check("Your answer: ")
        if user_answer == answer:
            result = "Correct"
            score += 1
        else:
            result = "Incorrect"
    except ValueError:
        user_answer = "Invalid"
        result = "Invalid input"
# print history and end of game
    history_entry = (f"\nRound {rounds_played + 1}: {num1} {operator} {num2} = {answer} | "
                     f"Your answer: {user_answer} - {result}")

    game_history.append(history_entry)

    rounds_played += 1

print("Game Over")
print(f"\nYou got {score} out of {num_rounds} correct.\n")
percentage = (score / num_rounds) * 100
print(f"\nYou got {percentage:.1f}% correct.")
print()
print("Game History:")
for item in game_history:
    print(item)


print()
print("Thank you for playing Quiz quest.")
