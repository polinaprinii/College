"""
Exercise 1
Ask the user to input for a number. Check whether the number is even or odd,
print out an appropriate message to the user.
"""
# Input clause to retrieve initial number for analysis.
num = int(input("Please enter a number for the machine to determine if it is even or odd."))

# If statement to determine whether number is odd or even.
if (num % 2) == 0:
    print("{0} is an Even number".format(num))
else:
    print("{0} is an Odd number".format(num))

"""
Exercise 2
Ask the user for a string and print out whether this string is a palindrome or not. A palindrome is a string
that reads the same forwards and backwards.
"""

# Input for a string.
text = input("Please enter a word here, the machine will tell if the word is a palindrome or not.")
reverse = reversed(text)

# If statement to determine if word is a palindrome word.
if list(text) == list(reverse):
    print("The provided is a palindrome word.")
else:
    print("The provided is not a palindrome word.")

"""
Exercise 3
Write a program that takes a list of numbers (for example, a = [10, 25, 9, 23]) and 
create a new list with the first and last elements of the given list.
"""
# Creating a list.
mylist = [1, 2, 3, 4, 5]
print(mylist)

# Using indexes we create a new list with the first and last element of the previous list.
newlist = [mylist[0], mylist[-1]]
print(newlist)

"""
Exercise 4
Write a function that takes a list of numbers. The function decides whether or not the given number 
is inside the list and returns an appropriate Boolean.
"""

numberlist = [1, 2, 3, 4, 5]
var = input("Enter a number to see if it is the list or not.")


def listcheck():
    if var in numberlist:
        print("Yes the number provided is in our list.", "\n")

    else:
        print("No the number provided is not in our list")

listcheck()
