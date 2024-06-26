import WordleAPI

# Main Code
if __name__ == "__main__":
    solver = WordleAPI.Solver()

    # Main Loop
    while solver.get_words_left() > 1:
        # Print Best Guess
        print(f"Best Guess: {solver.get_best_guess()}")
        print(f"Words Left {solver.get_words_left()}")

        # Input Entered Guess
        guess = input("Enter word: ")

        # Break
        if guess == "": break

        # {index: [char, color]}
        guess_dict = {}

        # Get Colors
        print()
        print(f"Gray: {WordleAPI.gray}\nYellow: {WordleAPI.yellow}\nGreen: {WordleAPI.green}\n")
        for index, char in enumerate(guess):
            guess_dict[index] = [char, input(f"Enter {char} color: ")]

        # Update Possible Words
        solver.update_possible_words(guess_dict)
        print()
    input(solver.get_best_guess())
