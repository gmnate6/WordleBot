from .game import Game
from .solver import Solver
from .utils import get_word_list
from .utils import export_csv

def test_word(word: str) -> list[str, int]:
    game = Game(word)
    solver = Solver()

    while True:
        result = game.make_guess(solver.get_best_guess())

        # Check for Win
        if result is True:
            return [word, game.guesses]
        solver.update_possible_words(result)

        # Check for Lose
        if solver.get_words_left() == 0:
            return [word, 0]

def run_test() -> list[list[str, int]]:
    word_list = get_word_list()
    results: list[list[str, int]] = [["Word:", "Guesses Took:"]]

    # Test Each Word
    for word in word_list:
        result = test_word(word)

        # Print
        print(result)
        print()

        # Update Reults
        results.append(result)

    # Export Results
    export_csv("results.csv", results)

    # Return Results
    return results
