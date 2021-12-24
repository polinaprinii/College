#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Week 2 - Lab @ Wednesday 29th Sept
#Q1: Using the type function, determine the datatype of the following literal values:

a = type('a')
b = type('abcd')
c = type(u'abcd')
d = type("x")
e = type("yz")
f = type(122)
g = type(0o2)
h = type(0x9)
i = type(0x2)
j = type(True)
k = type('true')
l = type((1,2))
m = type(["1", 2])
n = type({123: "abc", 345: "alive"})
     

print(a, b, c,d, e, f,g, h, i, j, k, l, m, n)


# In[33]:


#Q2

x = "a"
y = "a"
print(id(x))
print(id(y))
print('\n')
    
a = "anotherstring"
b = "anotherstring"
print(id(a))
print(id(b))
print('\n')

c = 'another string'
d = 'another string'
print(id(c))
print(id(d))

#A space in a string is the cause of having two different id's even though technically the value is the same.
#This is in regards to c and d.


# In[20]:


#Q3
#Create a list to store the following values: 1, 2, 3, 4, 5, 6 
#and assign this list to a variable called myList 

import random

#Print the contents myList

myList = [1, 2, 3, 4, 5, 6]
print(myList, '\n')

#Print the contents of myList in reverse using index slicing.

reversedList = []
reversedList = myList[6:None:-1]
print(reversedList, '\n')

#Print the contents of myList in reverse using a loop.

reversedListLoop = []
for a in reversed(myList):
    reversedListLoop.append(a)
print(reversedListLoop, '\n')

#Append 10 random integers to myList using a loop.

for a in range(10):
    myList.append(random.randint(1,10))
print(myList, '\n')

#Extend myList with the following list [200, 300] .
myList = [1, 2, 3, 4, 5, 6]
myList2 = [200, 300]
combinedList = myList + myList2
print(combinedList, '\n')

#Store the last number in the list in a variable called lastVal and remove that value from myList . 
#[Note: for this task you should investigate using the pop() method.]

lastVal = combinedList.index(300)
print(lastVal, '\n')
print(combinedList, '\n')

combinedList.pop(lastVal)
print(combinedList)


# In[30]:


#4 Create an empty dictionary object called myDict . 
#Using a loop structure, add an entry to myDict for each value in myList . 
#The key values for entries in myDict should be integer values commencing at 0 

myDict = {}

for i in range(len(myList)):
    myDict[i] = myList[i]
    
print(myDict)


# In[ ]:




