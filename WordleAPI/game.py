from .colors import *

class Game:
    def __init__(self, word: str):
        self.word = word
        self.guesses = 0
    
    def make_guess(self, guess: str) -> dict[int, list[str, str]]:
        # Add Guess
        self.guesses += 1

        # Return True if Won
        if guess == self.word:
            return True

        # Setup Colored Word
        colored_word = {}
        for index, char in enumerate(guess):
            # Green
            if self.word[index] == char:
                colored_word[index] = [char, green]
                continue

            # Yellow
            if char in self.word:
                colored_word[index] = [char, yellow]
                continue

            # Gray
            colored_word[index] = [char, gray]
        return colored_word
