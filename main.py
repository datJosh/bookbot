from stats import count_words, count_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_str = get_book_text('books/frankenstein.txt')
    count_words(book_str)
    count_characters(book_str)

main()