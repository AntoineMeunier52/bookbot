from stats import count_words
from stats import count_char
from stats import sort_chars
import sys

def main():
    filepath = check_arg(sys.argv)
    content = get_book_text(filepath)
    number_of_word = count_words(content)
    chars_dict = count_char(content)
    chars_list = sort_chars(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_word} total words")
    print("--------- Character Count -------")
    for char in chars_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")

def check_arg (args):
    if len(args) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return args[1]

def get_book_text (filepath):
    with open(filepath) as f:
        return f.read()


main()