from stats import get_number_of_words
from stats import number_of_each_character

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt") # Read the book's entire contents

    num_words = get_number_of_words(book_text) # Get the number of words in the book

    number_of_each_char = number_of_each_character(book_text) # Get the number of each character in the book

    print(f"Found {num_words} total words")  # Print the book's entire contents
    print(f"Found the following character counts: {number_of_each_char}")

main()