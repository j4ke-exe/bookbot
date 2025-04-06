import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    # Word count
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")

    # Character counts
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_char_counts(char_counts)

    print("\nCharacter frequencies (A–Z):")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read().lower()

main()