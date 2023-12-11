# your code goes here!
class Anagram:
  def __init__(self,word):
    self.word = word
  def match(self,word_list):
      return [ w for w in word_list if sorted(w) == sorted(self.word)]
  pass
anagram_instance = Anagram("listen")

# Define a list of words to test against the anagram
word_list = ["enlist", "silent", "hello", "yellow", "listen"]

# Use the match method to find anagrams in the word list
anagrams = anagram_instance.match(word_list)

# Print the result
print(f"Anagrams of '{anagram_instance.word}': {anagrams}")