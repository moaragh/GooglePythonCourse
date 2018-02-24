import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###


def word_count_d(filename): #Lets make a dictionary of words with their counts.. unsorted for now 
  word_counts_d={} # word_counts_d is a dictionary , keys are words, values are their counts
  file_input = open(filename, 'r')
  for line in file_input:
    words=line.split()
    for word in words:
      word=word.lower()
      if not word in word_counts_d:
        word_counts_d[word]=1
      else: 
        word_counts_d[word]+=1
  return word_counts_d

def print_words(filename):
  words_dict= word_count_d(filename) #Sorting keys which are words 
  words=sorted(words_dict.keys())
  for word in words:
    print(word,words_dict[word])
    
def WordCounterPerItem(word):
  return word[1]

def print_top(filename):
  words_dict= word_count_d(filename) #Sorting keys which are words 
  words=sorted(words_dict.items(),key=WordCounterPerItem, reverse=True)
  for word in words[:20]:
    print (word[0], word[1])
    

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()