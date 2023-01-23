# Hangman game in python console

import random
from drawing import gallows


# Grab words from a list, according to minimum length set by player
class Hangman:
    def __init__(self):
        self.words = None
        self.word = ""
        self.guesses = 0
        self.guessed = []
        self.word_completion = ""
        self.game_over = False
        self.word_completion = ""

    def grab_words(self, x, y):
        with open("words.txt") as f:
            self.words = f.read().splitlines()
        try:
            self.words = [self.word for self.word in self.words if x <= len(self.word) <= y]
            self.word = random.choice(self.words).upper()
            self.word_completion = "".join(["_" for letter in self.word]).upper()
            self.print_hangman(0)
            print(self.word_completion)
        except IndexError:
            print(
                f"Exiting game as no word found, try again next round with a shorter word length.")
            exit()

    def get_guess(self):
        while True:
            guess = input("Guess a letter: ").upper()
            if len(guess) != 1:
                print("One letter guess at a time")
            elif guess in self.guessed:
                print("You already guessed that letter!")
            elif not guess.isalpha():
                print("You can only guess letters!")
            else:
                return guess

    def play(self):
        while not self.game_over:
            self.display_progress()
            p1_guess = self.get_guess()
            if p1_guess not in self.word:
                print(f"{p1_guess} is not in the word!")
                self.guessed.append(p1_guess)
                self.guesses += 1
                self.print_hangman(self.guesses)

                if self.guesses == len(gallows)-1:
                    self.game_over = True
                    print(f"Unlucky! You're out of guesses! The word was {self.word}")
            else:
                print(f"Good guess! {p1_guess} is in the word!")
                self.guessed.append(p1_guess)
                self.update_progress(p1_guess)

    def update_progress(self, guess):
        partial_complete = list(self.word_completion)
        idx = [idx for idx, letter in enumerate(self.word) if letter == guess]
        for i in idx:
            partial_complete[i] = guess
        self.word_completion = "".join(partial_complete).upper()
        self.print_hangman(self.guesses)
        print(self.word_completion)
        if "_" not in self.word_completion:
            self.game_over = True
            print("You win!")

    @staticmethod
    def print_hangman(guesses):
        print(gallows[guesses])

    def display_progress(self):
        print(f"Guesses left: {len(gallows)-self.guesses-1}")


def main():
    # Set up game
    print("Welcome to Hangman!\n Please pick a mode:")
    print("""1. Easy
2. Medium
3. Hard""")
    game = Hangman()
    try:
        mode = int(input("Enter mode: "))
        if mode == 1:
            game.grab_words(2, 5)
        elif mode == 2:
            game.grab_words(6, 11)
        elif mode == 3:
            game.grab_words(12, 20)
        game.play()
    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    main()
