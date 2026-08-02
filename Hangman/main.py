import random
from hangman_words import word_list
from hangman_art import logo, stages

# Print the Hangman logo when the game starts
print(logo)

# Randomly choose one word from the word list
chosen_word = random.choice(word_list)

# Create a list of underscores (_) equal to the length of the chosen word
display = []

for letter in chosen_word:
    display.append("_")

# Player starts with 6 lives
lives = 6

# Store all guessed letters
guessed_letters = []

# Controls the game loop
game_over = False

# ==========================
# Main Game Loop
# ==========================
while not game_over:

    # Show the current progress of the word
    print("\nWord:", " ".join(display))
    print(f"Lives Remaining: {lives}")

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # --------------------------
    # Validate the input
    # --------------------------
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE alphabet.")
        continue

    # --------------------------
    # Check if the letter has already been guessed
    # --------------------------
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    # Save the guessed letter
    guessed_letters.append(guess)

    # --------------------------
    # Check if the guess is correct
    # --------------------------
    if guess in chosen_word:

        # Reveal every occurrence of the guessed letter
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess

        print("Correct! ✅")

    else:
        # Wrong guess
        lives -= 1
        print(f"'{guess}' is not in the word.")
        print("You lose a life. ❌")

    # Display the current Hangman stage
    print(stages[lives])

    # --------------------------
    # Check Win Condition
    # --------------------------
    if "_" not in display:
        game_over = True
        print("\n🎉 Congratulations! You Win!")
        print("The word was:", chosen_word)

    # --------------------------
    # Check Lose Condition
    # --------------------------
    elif lives == 0:
        game_over = True
        print("\n💀 Game Over!")
        print("The word was:", chosen_word)