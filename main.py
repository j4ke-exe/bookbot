from stats import get_num_words, get_char_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    char_counts = get_char_count(book_text)
    print("\nCharacter frequencies:")
    print(char_counts)

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

main()