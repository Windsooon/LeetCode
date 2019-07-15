
def shortestWordEditPath(source, target, words):
    count = 0
    return shortestWordEditPathRecur(source, target, words, count)

# find all words that are within edit distance one to the source
# for each one of these words I want to call the function again, with source = word
# source == target or -1 


def shortestWordEditPathRecur(source, target, words, count):
  if source == target:
    return count
  
  edit_words = find_edit_words(source,words)
  for word in edit_words:
    new_words = words[:]
    new_words.remove(source)
    count = shortestWordEditPathRecur(word,target, new_words, count+1)
    if count:
        return count
    
def find_edit_words(source,words):
  # problem is in this function
  source_chars = list(source)
  edit_words = []
  for word in words:
    if word == source:
      continue
    curr_word_chars = list(word)
    if is_edit(source_chars, curr_word_chars):
      edit_words.append(word)
  return edit_words      
    
    
def is_edit(chars_s, chars_t):
  if len(chars_s) != len(chars_t):
    return False
  mismatch_counter = 0
  for char_s, char_t in zip(chars_s,chars_t):#do we need to the *?
    if char_s != char_t:
      mismatch_counter +=1
      
  return mismatch_counter == 1 
    

source = "bit"
target = "dog"
words = ["bit", "but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortestWordEditPath(source, target, words))
