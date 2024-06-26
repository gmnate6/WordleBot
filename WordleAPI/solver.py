import os

from .colors import *
from .utils import get_word_list
from .utils import get_char_frequencies
from .utils import get_char_frequencies_from_list

# Solver Class
class Solver:
    def __init__(self):
        self.load_possible_words()
        self.possible_words_char_frequencies = get_char_frequencies_from_list(self.possible_words)

    def load_possible_words(self):
        self.possible_words = get_word_list()
    
    def reset(self):
        self.load_possible_words()

    def update_possible_words(self, word_dict: dict[int, list[str, str]]):
        # Do nothing if None
        if word_dict is None:
            return

        # Sets for characters and conditions
        gray_chars = {char.lower() for index, (char, color) in word_dict.items() if color == gray}
        yellow_conditions = [(index, char.lower()) for index, (char, color) in word_dict.items() if color == yellow]
        green_conditions = [(index, char.lower()) for index, (char, color) in word_dict.items() if color == green]

        # Word Fits
        def word_fits(word: str) -> bool:
            word_lower = word.lower()
            # Check for gray characters
            if any(char in word_lower for char in gray_chars):
                return False
            # Check for yellow conditions
            if any(word_lower[index] == char or char not in word_lower for index, char in yellow_conditions):
                return False
            # Check for green conditions
            if any(word_lower[index] != char for index, char in green_conditions):
                return False
            return True

        # Filter possible words
        self.possible_words = [word for word in self.possible_words if word_fits(word)]

    def get_word_score(self, word: str) -> int:
        # Unique Chars
        unique_chars = len(set(word))
        score = unique_chars

        # Update Possible Words Char Frequencies
        if self.get_words_left() <= 1000:
            self.possible_words_char_frequencies = get_char_frequencies_from_list(self.possible_words)

        # Frequent Chars
        word_char_frequencies = get_char_frequencies(word)
        for char in word_char_frequencies:
            if word_char_frequencies[char] > 1:
                continue
            score += self.possible_words_char_frequencies[char]
        return score

    def get_best_guess(self) -> str:
        if not self.possible_words:
            return None
        return max(self.possible_words, key=self.get_word_score)

    def get_words_left(self) -> int:
        return len(self.possible_words)
