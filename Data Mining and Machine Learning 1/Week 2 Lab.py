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

counts = Counter(frequency_dict)
top_word = counts.most_common(1)
least_word = counts.most_common()[-1]
print("The most frequent word is ", top_word, "\n")
print("The least frequent word is ", least_word, "\n")

