import random

# Predefined list of words
words = ["apple", "house", "plane", "chair", "table"]

# Select a random word
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Create a display version of the word (e.g., _ _ _ _ _)
display_word = ["_" for _ in word_to_guess]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.")

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nCurrent word: ", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
        # Reveal the guessed letter in the display word
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} incorrect guesses left.")

# Game over condition
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame over! The word was:", word_to_guess)
