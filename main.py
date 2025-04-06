def main():
   book_text = get_book_text("/books/frankenstein.txt")
   print(book_text)
   
def get_book_text(filepath):
   with open(filepath, "r") as f:
      return f.read()
   
main()