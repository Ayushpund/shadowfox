import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.secret_word = random.choice(words)
        self.guesses_left = 6
        self.guessed_letters = set()
        self.progress = ['_'] * len(self.secret_word)

    def display_progress(self):
        print(" ".join(self.progress))
        print(f"Guesses left: {self.guesses_left}")

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You've already guessed that letter.")
            return
        self.guessed_letters.add(letter)
        if letter in self.secret_word:
            print("Correct guess!")
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.progress[i] = char
        else:
            print("Incorrect guess!")
            self.guesses_left -= 1

    def get_hint(self):
        hint = random.choice(self.secret_word)
        while hint in self.guessed_letters:
            hint = random.choice(self.secret_word)
        print(f"Hint: {hint}")

    def play(self):
        print("Welcome to Hangman!")
        self.display_progress()
        while self.guesses_left > 0 and '_' in self.progress:
            guess = input("Guess a letter: ").lower()
            if guess == 'hint':
                self.get_hint()
            else:
                self.guess_letter(guess)
            self.display_progress()
        
        if '_' not in self.progress:
            print("Congratulations! You guessed the word correctly.")
        else:
            print(f"Sorry, you ran out of guesses. The word was {self.secret_word}.")

# List of words for the game
words = ["python", "hangman", "programming", "computer", "game", "learning"]

# Create an instance of Hangman game
game = Hangman(words)

# Start the game
game.play()
