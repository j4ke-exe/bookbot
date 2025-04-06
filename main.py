def main(get_book_text):
   with open("/books/frakenstein.txt") as f:
      file_contents = f.read()
      print(file_contents)
   
main()