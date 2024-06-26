import customtkinter as ctk

from .game_frame import GameFrame

# App Class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Screen Setup
        self.title("Wordle Bot")
        self.geometry("435x477")
        self.resizable(False, False)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        # Load Screen
        self.load()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def load(self, screen=GameFrame):
        self.clear()
        screen = screen(master=self)
        screen.pack(fill="both", expand=True)
        screen.load()

    def close(self):
        self.destroy()
