

def get_num_words(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  #print (file_contents)
  word_list = file_contents.split()
  #print (word_list)
  num_words = len(word_list)
  return num_words  

def count_characters(input_text_string):
  results_dictionary = {}
  for char in input_text_string:
    char.lower()
    if char.lower() in results_dictionary:
      current_count = results_dictionary[char.lower()]
      current_count = current_count+ 1;
      results_dictionary[char.lower()] = current_count
    else:
      results_dictionary[char.lower()] = 1
  return results_dictionary

