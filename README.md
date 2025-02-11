# WordleBot
WordleBot is a Python-based application that automatically solves the game of Wordle. It uses a Custom Tkinter UI for a user-friendly interface and a specialized Wordle module for the game logic.

## Features
- Wordle Solver: The bot solves any given Wordle puzzle based on the feedback from the game (correct, wrong, or mispositioned letters).
- Custom UI: Built using Custom Tkinter, the application provides a simple and interactive interface to play the game.
- Efficient Algorithm: The solver uses a dictionary of possible words and filters out incorrect guesses based on the clues provided during each round of the game.
- Full Game Logic: The WordleBot holds all the necessary game logic, including feedback interpretation and guess generation.

## Technologies Used
- Python 3.x: Core language for implementation.
- Tkinter: For building the graphical user interface (GUI).
- Custom Wordle Module: Handles the logic of solving Wordle puzzles.

## Installation
To run WordleBot locally, follow these steps:

1. Clone the repository:
git clone https://github.com/gmnate6/WordleBot.git

2. Navigate into the project directory:
cd WordleBot

3. Install dependencies:
pip install -r requirements.txt

4. Run the application: Launch the bot by running:
python main.py

The Tkinter GUI should open, and you can start playing the game.

## How to Play
1. Enter your Wordle guess into the interface.
2. Click to color the tiles.
3. The bot will use the feedback to make the next guess and solve the puzzle.

## Contributing
Feel free to fork the repository and create pull requests. If you'd like to contribute, please make sure to follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request for review.

## License
This project is open source and available under the MIT License.

Acknowledgments
- Thanks to Wordle for inspiring this project!
- Special mention to Tkinter and Python’s powerful libraries for making this application possible.
