# Hangman game I watned to try out


import random

# List of words
words = ["Plyometrics", "Sakamoto", "hangman", "computer", "Southwest", "Crocodile"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # number of wrong guesses allowed

    print("🎮 Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
