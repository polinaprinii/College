# Tokeniser Problem

"""
1)
Take a text file (uploaded to Moodle) as an input of your program. 
Read its content. Write frequency of the words of the text in a file. 
Use python’s dictionary data structure for storing frequencies of the words. 
[hint: consider word as key and frequency of that word as value]
"""

# Creating an empty dictionary which will hold our word frequencies.
frequency_dict = {}

# Importing text file into PyCharm
textfile = open("/Users/polinaprinii/Downloads/Lab - Python Exercise Tokeniser Problem.en-fr.en", "r")
# Printing our variable for verification purposes.

# Loop through each line of the file
for line in textfile:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in frequency_dict:
            # Increment count of word by 1
            frequency_dict[word] = frequency_dict[word] + 1
        else:
            # Add the word to dictionary with count 1
            frequency_dict[word] = 1

# Print the contents of dictionary
for key in list(frequency_dict.keys()):
    print(key, ":", frequency_dict[key], "\n")

textfile.close()

"""
2)
Write most- and least-frequent words (100) in a file.
"""

from collections import Counter

# Setting Counter to our dictionary and assigning all to a variable.
counts = Counter(frequency_dict)

# Searching for the most common/frequent word.
top_word = counts.most_common(1)

"""Searching for least common/frequent word.
We must use indices as Counter does not provide a least common clause.
Instead we specify to look at the end of the dict
"""
least_word = counts.most_common()[-1]

print("The most frequent word is ", top_word, "\n")
print("The least frequent word is ", least_word, "\n")

"""
Count total number of words and total number of unique words in the corpus.
[corpus is a collection of text; here, set of sentences of the text file is referred as corpus].
"""
file = open("/Users/polinaprinii/Downloads/Lab - Python Exercise Tokeniser Problem.en-fr.en", "rt")
data = file.read()
words = data.split()

print('Number of words in our text file is: ', len(words), "\n")

# Finding number of unique words within the text file.
unique_words = set(words) # Using set() to convert our dictionary of multiple items to one single variable of distinct elements.
unique_word_count = len(unique_words)
print("The number of unique words in the text file is: ", unique_word_count, "\n")
