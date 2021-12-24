#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[24]:


#1 Character strings

# Create a short piece of Python code that prompts the user to enter a string and then prints 
# the first, third and fifth characters in the string.

my_str = input("Enter a string: ")
string = my_str[0] + my_str[2] + my_str[4] #For specific character indexing regardless of string size we 
# specify each slices and add them using +.
print(string)


# In[29]:


# 2 ID and Class

# Write some Python code that creates two variables, one variable a with an integer value and another 
# variable b with a floating point value. Then print the id and class of both variables.

var1 = 1
var2 = 9.0

print("ID of var1 is:", id(var1), "\n")
print("Class of var1 is:", type(var1), "\n")
print("ID of var2 is:", id(var2), "\n")
print("Class of var2 is:", type(var2), "\n")


# In[30]:


#3 Boolean values
# Create a snippet of Python code to test if the following are equivalent to False:

if not None : print ('None is False')
str = ""
if not str : print ('str is False')
lists = []
if not lists : print ('lists is False')
sets = {}
if not sets : print ('sets is False')
tuples = ()
if not tuples : print ('tuples is False')


# In[32]:


#4 String replacement
#Complete the code below so that the word ‘Bachelors’ is replaced with ‘Masters’. 
#Then print the resulting string.

degree = "Bachelors in Data Analytics"
print("Original text is:", degree, "\n")

x = degree.replace("Bachelors", "Masters")
print("Corrected text is:", x)


# In[ ]:




