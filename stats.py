def count_words(book_text):
    """
    Counts the number of words in the given book_text string.
    Args:
        book_text (str): The text of the book.
    Returns:
        int: The number of words in the book text.
    """
    return len(book_text.split())   # Return the number of words by splitting the text into words and counting them

def count_characters(book_text):
    """
    Counts the number of characters in the given book_text string.
    Args:
        book_text (str): The text of the book.
    Returns:
        int*n: The nunber of times each character appears in the book text.
    """
    characters = {}

    for character in book_text:
        char = character.lower()
        if char in characters:
            characters[f"{char}"] += 1
        else:
            characters[f"{char}"] = 1
    return characters

def sort_text(char_dict):
    """
    Upon review, it was suggested I use: 'key=lambda item: item["num"]'
    instead of defining a new inner function.
    But I don't understand this yet, so I'll leave it here for when I do.
    """
    def sort_magic(item):
        return item["num"]  # This is still a bit brain-numbing... sort() using a function
    sorted_list = []
    for key in char_dict:
        value = char_dict[key]
        mini_dict = {}
        mini_dict["char"] = key
        mini_dict["num"] = value
        sorted_list.append(mini_dict)
    # sorted_list = [{"char": key, "num": value} for key, value in char_dict.items()]
    sorted_list.sort(reverse=True, key=sort_magic) 
    return sorted_list

## Test/Debugging code
# for item in sort_text(count_characters("You Dumb-Dumb, give me gum-gum")):
#     print(item)
