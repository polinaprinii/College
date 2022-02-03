# Tokeniser Problem

"""
Take a text file (uploaded to Moodle) as an input of your program. 
Read its content. Write frequency of the words of the text in a file. 
Use python’s dictionary data structure for storing frequencies of the words. 
[hint: consider word as key and frequency of that word as value]
"""

# Creating an empty dictionary which will hold our word frequencies.
frequency = {}

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
        if word in frequency:
            # Increment count of word by 1
            frequency[word] = frequency[word] + 1
        else:
            # Add the word to dictionary with count 1
            frequency[word] = 1

# Print the contents of dictionary
for key in list(frequency.keys()):
    print(key, ":", frequency[key])

"""
Write most- and least-frequent words (100) in a file.
"""





