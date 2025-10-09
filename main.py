from stats import get_num_words
from stats import count_characters

def main():
  #get_book_text("books/frankenstein.txt")
  num_words = get_num_words("books/frankenstein.txt")
  book_as_string = get_book_text_as_string("books/frankenstein.txt")
  characters_only = count_characters(book_as_string) 

  print(f"Found {num_words} total words")
  print(characters_only)

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  print(file_contents)

def get_book_text_as_string(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

#def show_report(file_location):
#

  

main()
