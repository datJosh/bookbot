def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_str = get_book_text('books/frankenstein.txt')
    print(book_str)

main()