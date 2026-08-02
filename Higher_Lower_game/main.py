from game_data import data
from art import vs, logo
import random

print(logo)

score = 0
game_should_continue = True

A = random.choice(data)
B = random.choice(data)

while B == A:
    B = random.choice(data)

while game_should_continue:
    print(f"Compare A: {A['name']}, {A['description']}")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if A["follower_count"] == B["follower_count"]:
        correct_answer = guess.upper()
    elif A["follower_count"] > B["follower_count"]:
        correct_answer = "A"
    else:
        correct_answer = "B"

    if guess.upper() == correct_answer:
        score += 1
        print(f"Correct! Your score is {score}.")

        A = B
        B = random.choice(data)
        while B == A:
            B = random.choice(data)
    else:
        print(f"Wrong! Final score: {score}")
        game_should_continue = False