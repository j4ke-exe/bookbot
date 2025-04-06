from stats import get_num_words, get_char_count, sort_char_count

def main():
    book_text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    char_counts = get_char_count(book_text)
    sorted_chars = sort_char_count(char_counts)

    print("\nCharacter frequencies (A–Z):")
    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['count']} times")

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

main()