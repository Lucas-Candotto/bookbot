import sys
import os
from stats import get_num_words, get_characters, sort_char_count
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
def main():
    with open(book_path) as f:
        file_contents = f.read()
    word_count = get_num_words(file_contents)
    char_count_dict = get_characters(file_contents)
    sorted_chars = sort_char_count(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
if __name__ == "__main__":
    main()