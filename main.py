import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(p):
    with open(p) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_str = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    count_words(book_str)
    print("--------- Character Count -------")
    chars = sort_characters(count_characters(book_str))
    for char in chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
main()