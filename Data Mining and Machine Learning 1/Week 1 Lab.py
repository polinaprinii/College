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
