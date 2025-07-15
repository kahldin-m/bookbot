import stats
import sys
import os

def main():
    """
    Main function to run the BookBot application.
    It checks command line arguments, reads the book file, counts words and characters,
    and prints the results.
    """
    if len(sys.argv) <= 1:
        print("Hello world! BookBot is used to analyze books. It will count words and characters and print the results!\n- Usage: python3 main.py <path_to_book> (ex, books/frankenstein.txt)\n- To check available books: python3 main.py booklist")
        exit(1)
    if sys.argv[1] == "booklist":
        books = os.listdir("books/")
        print("Available books at path 'books/':")
        for book in books:
            print(f"- {book}")
        exit(0)
    book_to_read = sys.argv[1]
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_to_read}...
----------- Word Count ----------""")
    book_text = stats.get_book_text(sys.argv[1])
    num_words = stats.count_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_characters = stats.sort_text(stats.count_characters(book_text))
    for character_dict in list_of_characters:
        # Check if the character is alphabetical before printing
        if character_dict["char"].isalpha():
            char_name = character_dict["char"]
            char_count = character_dict["num"]
            print(f"{char_name}: {char_count}")
    print("============= END ===============")

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"{e}.\n[Remedy] Please ensure the book file exists and the path is correct. Example path: books/frankenstein.txt")