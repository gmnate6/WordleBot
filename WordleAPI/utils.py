import os
from collections import Counter
import csv

def get_char_frequencies(word: str) -> Counter:
    return Counter(word.lower())

def get_char_frequencies_from_list(word_list: list[str]) -> Counter:
    return Counter(char for word in word_list for char in word.lower() if char.isalpha())

def get_word_list() -> list[str]:
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "words.txt")
    with open(file_path, "r") as file:
        lines = file.readlines()
        word_list = [line.strip() for line in lines]
    return word_list

def export_csv(file_name: str, data: list[list[str, int]]):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
