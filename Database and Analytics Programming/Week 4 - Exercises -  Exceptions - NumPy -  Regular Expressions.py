#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Week 4 Lab - NDarrays

# 1 Creating, reshaping and slicing n-dimensional arrays.

import numpy as np
arr1 = np.arange(24)
print("Array from 0 to 23:")
print(arr1, '\n')

arr3 = arr1.reshape(2, 3, 4)
print("New array looks like this: ")
print(arr3, '\n')

print(arr3[0, :])


# In[15]:


# 2 Slicing n-dimensional arra

import numpy as np
a = np.array(
  [[[12,11,10],
    [9,8,7]],
   [[1,2,3],
    [4,5,6]]])

print(a, '\n')

print("From the second matrix, row 2 and column 2 and 3 we have: ", a[1, 1, 1:])


# In[43]:


# Week 4 - Exceptions & Regular Expressions

# 1 Parsing dates and raising exceptions

import re
from datetime import datetime

x = input('Please input date in the format YYYY-mm-dd ')
dateList = []

format = "%Y-%m-%d"


try:
    datetime.strptime(x, format)
    year = re.search(r"\d{4}", x).group(0)
    dateList.append(year)
    print(dateList)
except ValueError:
    print("This is the incorrect date string format. It should be YYYY-MM-DD")


# In[ ]:





# In[ ]:




