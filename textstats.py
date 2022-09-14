#[10 points] Write a Python application to take a plain text document as input, compute a number of
#statistics on the contents of the document, and allow users to query for information.
#Your application should keep counts of each word found in the document. For example, if I passed a
#text document containing the following text to your app:
#The quick brown fox jumps over the lazy dog.
#Your application should calculate and store the following counts:
#“the”: 2
#“quick”: 1
#“brown”: 1
#“fox”: 1
#“jumps”: 1
#“over”: 1
#“lazy”: 1
#“dog”: 1
#Users should then be given an input prompt, and able to query the count of a given word. A user session
#might look like this:
#$ python textstats.py input.txt
# Text document analyzed. Enter a word at the prompt to see its statistics.

# Enter a word: _
#$ python textstats.py input.txt
# Text document analyzed. Enter a word at the prompt to see its statistics.

# Enter a word: fox
# Statistics for the word “fox”:
# count: 1

# Enter a word: _
#$ python textstats.py input.txt
# Text document analyzed. Enter a word at the prompt to see its statistics.

# Enter a word: fox
# Statistics for the word “fox”:
# count: 1


# Opening our text file in read only
# mode using the open() function
from operator import truediv
from os import linesep


with open(r'input.txt','r') as file:

 # Reading the content of the file
 # using the read() function and storing
 # them in a new variable
 data = file.read()

 # Splitting the data into separate lines
 # using the split() function
 lines = data.split()

print("Text document analyzed. Enter a word at the prompt to see its statistics.")
word = input('Enter your name:')

count = 0
for item in lines:
    if item == word:
        count += 1
print("Statistics for the word:", word)        
print("Count:", count)





