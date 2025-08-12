def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    words = str.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main():
    book_str = get_book_text('books/frankenstein.txt')
    count_words(book_str)

main()