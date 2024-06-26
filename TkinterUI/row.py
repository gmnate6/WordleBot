import customtkinter as ctk

from .tile import Tile

# Row Class
class Row(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=285,
            height=52,
            corner_radius=0,
            fg_color="transparent",
        )
        self.current_column = 0
        self.load()

    def get_colored_word(self) -> dict[int, list[str, str]]:
        if self.is_filled() is False:
            return None

        # Get Guess Dict
        colored_word = {}
        for column in range(5):
            tile = self.tiles[column]
            colored_word[column] = [tile.get_letter(), tile.get_wordle_color()]
        return colored_word

    def gray_tiles(self):
        for tile in self.tiles:
            tile.gray_tile()

    def able(self):
        for tile in self.tiles:
            tile.able()
    
    def disable(self):
        for tile in self.tiles:
            tile.disable()
    
    def update_state(self):
        if self.is_filled():
            self.able()
        else:
            self.disable()
    
    def is_filled(self) -> bool:
        for tile in self.tiles:
            if tile.letter == "":
                return False
        return True

    def is_empty(self) -> bool:
        for tile in self.tiles:
            if tile.letter != "":
                return False
        return True
    
    def enter_letter(self, letter: str):
        if self.current_column > 4:
            return

        self.tiles[self.current_column].set_letter(letter)
        self.current_column += 1

        # Update State
        self.update_state()

    def delete_letter(self):
        # Return if last letter
        if self.current_column == 0:
            return

        # Delete Letter
        self.current_column -= 1
        self.tiles[self.current_column].set_letter("")

        # Gray All Tiles
        self.gray_tiles()

        # Update State
        self.update_state()

    def load(self):
        # Current Column
        self.current_column = 0

        # Tiles
        self.tiles: list[Tile] = []
        for x in range(5):
            tile = Tile(self)
            tile.grid(row=0, column=x, padx=(0, 5))
            self.tiles.append(tile)
        
        # Disable
        self.disable()
