#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Practice working with expressions, statements and program flow:

#1 Comparing strings

text_1 = input('Please type something here: ')
text_2 = input('Please type something here: ')

if text_1 == text_2:
    print('The text is the same')
else:
    print('The text is not the same')


# In[2]:


#2 Typecasting and exponentiation
#Write some Python code that prompts the user to enter a whole number. 
#You should then convert that number to an int, square it and print the result. 
#You can convert an int to a string using the str() typecasting function.

request = input('Please enter a whole number: ')
conversion = int(request)
result = str(conversion ** 2)

print(result)


# In[6]:


#3 Conditional statements
#Create a snippet of Python code to prompt the user to enter a temperature in Celsius. 
#You should convert this to a float. Then you should test the value and print one of the following:

    #The string ‘cold’ if the temperature is less than or equal to 10.
    #The string ‘warm’ if the temperature is greater than 10 and less than or equal to 25.
    #The string ‘hot’ if the temperature is greater than 25.

temp = int(input('Please specify temperature in celcius: '))
temp_conversion = float(temp)

if temp <= 10:
    print('cold')
elif temp > 10 and temp <= 25:
    print('warm')
elif temp >25:
    print('hot')


# In[28]:


#4 Repetition statements
#Write some Python code that repeatedly prompts the user to enter a string until the string entered is exactly 
#equal to ‘exit’ (without the quotes).

while True:
    x = input('Please type word here: ')
    if x == 'exit':
        break


# In[39]:


#Practice working with compound data types

#1 Lists
#Create a short piece of Python code that repeated prompts the user to enter items for a shopping basket 
#until the string ‘exit’ is entered (without the quotes). Each item entered should be added to a list 
#variable called shopping. When ‘exit’ is entered, the entire list should be printed.

myList = []

while True:
    x = input('Please add to the shopping list here: ')
    myList.append(x)
    if x == 'exit':
        myList.remove('exit')
        print(myList)
        break
        
    
        


# In[67]:


#2 Creating Multi-dimensional arrays
# Write some Python code that creates an ndarray with 4 rows and 5 columns, filled with all zeros. 
#Set the value in the first column and 3rd row to be equal to 3. 
#Set the value in the fourth column and second row to be equal to 5. Then print the contents of the ndarray.

import numpy as np

myMatrix = np.array([[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]])

print(myMatrix)
print('\n')

myMatrix1 = np.zeros((4, 5))
myMatrix1[2,0] = 3
myMatrix1[3,1] = 5
print(myMatrix1)

        


# In[103]:


#3 Operations on multi-dimensional arrays
#Create a snippet of Python code to create an ndarray of 5 rows and 5 columns filled 
#with all numbers from 1 to 25.

    #Find the sum of the entire ndarray.

    #Find the following:

        #the mean of each row
        #the mean of each column
        #the maximum value in each row
        #the minimum value in each column
        
import numpy as np
x = np.arange(start=1, stop=26).reshape(5, 5)


print(x, '\n')
print('Mean of x', + x.mean(axis=1), '\n')
print('Mean of y', + x.mean(axis=0), '\n')
print('Max of x', + x.max(axis=1), '\n')
print('Max of y', + x.max(axis=0), '\n')


# In[ ]:




