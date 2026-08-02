import random

number = random.randint(1, 100)

print("Choose a difficulty: easy or hard")
level = input("Type 'easy' or 'hard': ")

if level == "hard":
    attempts = 5
else:
    attempts = 10

print("I'm thinking of a number between 1 and 100.")

while attempts > 0:
    try:
        guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue

    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue

    if guess == number:
        print("Your guess is correct")
        break
    elif guess > number:
        print("Too high")
        attempts -= 1
        print(f"You have {attempts} attempts left")
    else:
        print("Too low")
        attempts -= 1
        print(f"You have {attempts} attempts left")
else:
    print(f"You lose. The number was {number}")