def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count(book_text)

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def word_count(book_text):
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document")

main()