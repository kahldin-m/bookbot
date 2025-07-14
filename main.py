from stats import count_words
from stats import count_characters
from stats import sort_text
import sys

def get_book_text(book_id):
    """
    Fetches the text of a book given its ID.
    Args: 
        book_id (str): The ID of the book to fetch.
    Returns:
        str: The text of the book.
    """
    # Open the book file using the provided book_id
    with open(book_id) as file:     # Open the file in read mode
        book_text = file.read()     # Read the contents of the file as "book_text"
    # Return the contents of the book
    return book_text

def main():
    """
    Does different things depending on the current Assignment
    """
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_to_read = sys.argv[1]
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_to_read}...
----------- Word Count ----------""")
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_characters = sort_text(count_characters(book_text))
    for character_dict in list_of_characters:
        # Check if the character is alphabetical before printing
        if character_dict["char"].isalpha():
            char_name = character_dict["char"]
            char_count = character_dict["num"]
            print(f"{char_name}: {char_count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()