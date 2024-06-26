import customtkinter as ctk
import tkinter as tk

import WordleAPI

from .row import Row
from .assets import UIColors
from .assets import UIFonts

# GameFrame Class
class GameFrame(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk):
        super().__init__(master, fg_color=UIColors.black, corner_radius=0)
        self.master.bind("<Key>", self.on_key_press)

    def reset(self):
        self.master.load()

    def get_best_guess(self) -> str:
        # Reset Wordle Solver
        self.wordle_solver.reset()

        # Update Wordle Solver
        for row in self.rows:
            self.wordle_solver.update_possible_words(row.get_colored_word())

        # Display Best Guess
        best_guess = self.wordle_solver.get_best_guess()
        if best_guess is None:
            best_guess = "[None]"
        self.best_guess_label.configure(text=best_guess)

        # Display Number of Words Left
        number_of_words = self.wordle_solver.get_words_left()
        self.num_of_words_left_label.configure(text=str(number_of_words))

        # Display List of Words Left
        list_of_words = ""
        for word in self.wordle_solver.possible_words:
            list_of_words += f"{word}\n"
        self.list_of_words_left_label.configure(text=list_of_words)

    def set_current_row(self, current_row: int):
        # Return if Current Row is out of range
        if current_row < 0 or current_row > 5:
            return
        self.current_row = current_row

    def on_key_press(self, event: tk.Event):
        if event.char.isalpha():
            # If Current Row is filled
            if self.rows[self.current_row].is_filled():
                # Update Current Row
                self.set_current_row(self.current_row + 1)
            # Enter Letter
            self.rows[self.current_row].enter_letter(event.char.upper())
        elif event.keysym == "BackSpace":
            # If Current Row is empty
            if self.rows[self.current_row].is_empty():
                # Update Current Row
                self.set_current_row(self.current_row - 1)
            # Delete Letter
            self.rows[self.current_row].delete_letter()
        elif event.keysym == "Return":
            # Print Best Guess
            self.get_best_guess()

    def load(self):
        # WordleBot
        self.wordle_solver = WordleAPI.Solver()

        # Main Frame
        main_frame = ctk.CTkFrame(self, width=300, height=477, fg_color="transparent", corner_radius=0)
        main_frame.grid(row=0, column=1)

        # Title
        title = ctk.CTkLabel(main_frame, height=45, fg_color="transparent", corner_radius=0, font=UIFonts.font45, text="WordleBot")
        title.pack(fill="both", expand=True, pady=(10, 0))

        # Game Frame
        game_frame = ctk.CTkFrame(main_frame, fg_color="transparent", corner_radius=0)
        game_frame.pack(fill="both", expand=True, padx=10, pady=10)
        # Rows
        self.rows: list[Row] = []
        for y in range(6):
            row = Row(game_frame)
            row.pack(pady=(0, 5))
            self.rows.append(row)
        self.set_current_row(0)

        # Bottom Frame
        bottom_frame = ctk.CTkFrame(game_frame, height=45, fg_color="transparent", corner_radius=0)
        bottom_frame.pack(fill="both", expand=True, pady=10)
        # Best Guess Button
        best_guess_button = ctk.CTkButton(
            bottom_frame,
            width=135, height=45,
            corner_radius=0,
            font=UIFonts.font16,
            text="Get Best\nGuess",
            fg_color=UIColors.green,
            hover_color=UIColors.gray,
            command=self.get_best_guess)
        best_guess_button.grid(row=0, column=1, padx=(0, 10))
        # Reset Button
        reset_button = ctk.CTkButton(
            bottom_frame,
            width=135, height=45,
            corner_radius=0,
            font=UIFonts.font16,
            text="Reset",
            fg_color=UIColors.green,
            hover_color=UIColors.gray,
            command=self.reset)
        reset_button.grid(row=0, column=2)

        # Side Frame
        side_frame = ctk.CTkFrame(self, width=130, corner_radius=0, fg_color=UIColors.black)
        side_frame.grid(row=0, column=2, sticky="nsew", padx=(0, 5))
        # Side Top Frame
        side_top_frame = ctk.CTkFrame(side_frame, width=120, height=45, corner_radius=0, fg_color=UIColors.gray)
        side_top_frame.pack(pady=10)
        side_top_label = ctk.CTkLabel(side_top_frame, width=120, height=25, corner_radius=0, font=UIFonts.font20, text="Words Left:")
        side_top_label.pack(pady=(2, 0))
        self.num_of_words_left_label = ctk.CTkLabel(side_top_frame, width=120, height=20, corner_radius=0, font=UIFonts.font20, text="")
        self.num_of_words_left_label.pack()

        # Words Left Scrollable Frame
        words_left_scrollable_frame = ctk.CTkScrollableFrame(side_frame, width=115, height=336, corner_radius=0, fg_color=UIColors.gray)
        words_left_scrollable_frame._scrollbar.configure(width=5, corner_radius=0, fg_color=UIColors.gray, hover=False)
        words_left_scrollable_frame.pack(pady=(0, 5))
        # List of Words Left Label
        self.list_of_words_left_label = ctk.CTkLabel(words_left_scrollable_frame, width=115, corner_radius=0, font=UIFonts.font20, text="")
        self.list_of_words_left_label.pack(padx=5, pady=5)

        # Best Guess Frame
        best_guess_frame = ctk.CTkFrame(side_frame, fg_color=UIColors.gray, width=120, height=45, corner_radius=0)
        best_guess_frame.pack(pady=10)
        label = ctk.CTkLabel(best_guess_frame, width=120, height=15, corner_radius=0, font=UIFonts.font16, text="Best Guess:")
        label.pack(pady=(2, 0))
        # Best Guess Label
        self.best_guess_label = ctk.CTkLabel(best_guess_frame, width=120, height=25, corner_radius=0, font=UIFonts.font16, text="")
        self.best_guess_label.pack()

        # Update WordleBot
        self.get_best_guess()
