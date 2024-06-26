import customtkinter as ctk

from WordleAPI import colors as WordleColors

from .assets import UIColors
from .assets import UIFonts

# Get UI Color
def get_ui_color(wordle_color: str) -> str:
    return {
        WordleColors.gray: UIColors.gray,
        WordleColors.yellow: UIColors.yellow,
        WordleColors.green: UIColors.green
    }[wordle_color]

# Tile Class
class Tile(ctk.CTkButton):
    def __init__(self, master):
        super().__init__(
            master,
            width=52,
            height=52,
            corner_radius=0,
            hover=False,
            font=UIFonts.font20,
            command=self.on_click
        )
        # Color
        self.ui_color = ""
        self.wordle_color = ""
        self.set_letter("")
        self.disable()
    
    def able(self):
        self.configure(state="normal")

    def disable(self):
        self.configure(state="disabled")

    def clear(self):
        self.set_letter("")
    
    def gray_tile(self):
        self.set_color(WordleColors.gray)

    def set_letter(self, letter: str):
        self.set_color(WordleColors.gray)
        self.letter = letter.upper()
        self.configure(text=self.letter)

    def get_letter(self) -> str:
        return self.letter

    def set_color(self, wordle_color: str):
        self.wordle_color = wordle_color
        self.ui_color = get_ui_color(wordle_color)
        self.configure(fg_color=self.ui_color)

    def get_wordle_color(self) -> str:
        return self.wordle_color

    def get_wordle_color(self) -> str:
        return self.wordle_color

    def on_click(self):
        if self.get_wordle_color() == WordleColors.gray:
            self.set_color(WordleColors.yellow)
        elif self.get_wordle_color() == WordleColors.yellow:
            self.set_color(WordleColors.green)
        elif self.get_wordle_color() == WordleColors.green:
            self.set_color(WordleColors.gray)
