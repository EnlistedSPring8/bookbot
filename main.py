from stats import get_number_of_words
from stats import number_of_each_character
from stats import sorted_character_count
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():

    if sys.argv and len(sys.argv) > 1:
        ref = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(ref) # Read the book's entire contents

    num_words = get_number_of_words(book_text) # Get the number of words in the book

    number_of_each_char = number_of_each_character(book_text) # Get the number of each character in the book

    sorted_chars = sorted_character_count(number_of_each_char) # Sort the character counts

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {ref}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")  # Print the book's entire contents
    print(f"------- Character Count -------")
    for chars in sorted_chars:               # Print each character and its count                      
        print(f"{chars["char"]}: {chars["num"]}")  

main()