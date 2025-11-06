#Notes for update. 6/11/25

from stats import get_num_words
from stats import count_characters
from stats import count_characters_highest_to_lowest

def main():
 #get_book_text("books/frankenstein.txt")
 #show_report("books/frankenstein.txt")
  characters_only = count_characters("Hello World") 
  print(characters_only)
  print("TEST LINE BREAK")
  #print(sort_on(characters_only))

  vehicles = [
      {"name": "car", "num": 7},
      {"name": "plane", "num": 10},
      {"name": "boat", "num": 2}
  ]
  vehicles.sort(reverse=True, key=sort_on)
  print(vehicles)
  print("TEST LINE BREAK")
  print()

def sort_on(items):
    return items["num"]



# def sort_on(items):
#     return items["num"]

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  print(file_contents)

def get_book_text_as_string(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents

def show_report(file_location):
# open the file, and get the result as a string#  
  num_words = get_num_words(file_location)
  book_as_string = get_book_text_as_string(file_location)
  characters_only = count_characters(book_as_string) 
  characters_high_low = count_characters_highest_to_lowest(book_as_string) 

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_location}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  print(characters_only)
  print("============= END ===============")


main()
