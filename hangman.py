import random

words = ["PYTHON", "COMPUTER", "PROGRAM", "COLLEGE", "STUDENT"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

hangman_pictures = [
    r"""
  +---+
  |   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
=========""",
]

print("Welcome to the Hangman Game!!!")

while incorrect_guesses < max_guesses:
    print(hangman_pictures[incorrect_guesses])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    if all(letter in guessed_letters for letter in word):
        print("CONGRATULATIONS!! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").upper().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print(hangman_pictures[incorrect_guesses])
    print("\nGAME OVER!! The word was:", word)