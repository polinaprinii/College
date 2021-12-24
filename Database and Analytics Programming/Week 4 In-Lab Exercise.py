#!/usr/bin/env python
# coding: utf-8

# In[18]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[49]:


#In-Lab Exercises:

#Exception Handling Exercise

#1) Create a text file and manually add some data to the file.

my_file = open("myfile.txt", "w")
my_file.write("Hello, here is some text for the ")


# In[ ]:


#2) Write Python code to
    # open the file for write only access
    # attempt to read the contents of the file
    
open_file = open("myfile.txt", "w")
#print(open_file.read()) 

# 3) Note the type of Error that has been raised: 

    # UnsupportedOperation: not readable
    


# In[ ]:


# 4) Modify your code to:
    # use a try / except / finally construct that will catch the exception, 
    #print a user- friendly error message, and clean up the file resource
    
try:
    final_ex = open("myfile.txt", "w")
    print(open_file.read())
    
except IOError:
    print("Could not open: ", final_ex, "as we have specified mode as W = writeable")

finally:
    final_ex.close()
    


# In[ ]:


#5) Investigate how you would create your own Exception class. 
# Then create your own Exception class and use it in your code from the previous exercise.

class myerror(Exception):
    pass


# In[11]:


# NumPy Exercise 1

# 1) Create an array with the arange function and reshape the array as follows:
    # b = arange(24).reshape(2,3,4)
    
import numpy as np

arr = np.arange(24)
print(arr, "\n")

arr1 = arr.reshape(2, 3, 4)
print(arr1, "\n")

# Using indexing and slicing perform the following tasks:
    #i)Choose the first set of 3 rows and 4 columns of data

print("i) The first 3 rows and 4 columns of data are: ","\n", arr1[0, 0:], "\n")

    #Choose the second row of data from the second set of 3 rows of data
    
print("ii) The second row of data from the second set is: ", "\n", arr1[1, 1, 0:], "\n")

    #Choose all the data from the second column for both the first and second sets of rows and columns of data.

print("iii) a) The 2nd column data for each row for each set is: ", "\n", arr1[0, 0:, 1], arr1[1, 0:, 1], "\n")
print("iii) b) Another way of doing the above is this way: ", "\n", arr1[0:,0:,1:2], "\n") 
#The 1st bit is for data set being used, the 2nd bit is the rows being used and the 3rd bit is for the columns.
#Note the 1:2 mean it will only show column 2 (1) as it excludes column 3(2.)


# In[12]:


#2: 2) Use the ravel function to flatten the data. What’s the difference between ravel and flatten?

flatten_arr = arr1.ravel()
print("The array has been flattened, aka returned to a contiguous flattened array, a single line array: ", "\n", flatten_arr, "\n")


# In[13]:


#3) Reshape the data so that there are 6 rows of 4 columns per row.

reshaped_arr = flatten_arr.reshape(6, 4)
print("Reshaped array to 6 rows & 4 columns: ", "\n", reshaped_arr, "\n")


# In[14]:


#4) Get the transpose of the new data structure.

b = np.transpose(reshaped_arr)  
print("Transposed array: ", "\n", b, "\n")


# In[15]:


#5) Restack the rows of the transposed data structure in reverse order (hint: look at the row_stack function).

c = np.row_stack(b[::-1]) #create reversed view using [::-1] and at the same time apply the row_stack() function. 
print("Transposed array in reversed order: ", "\n", c, "\n") #[::-1] in python is a view which shows in reverse order.


# In[16]:


#6) Split the resulting data structure horizontally (hint: look at the hsplit function).

print("The data spilt horizontally: ", "\n", np.hsplit(c, 3))


# In[114]:


#NumPy Exercise 2

#1) Use the loadtxt command to load data from AAPL.csv from columns 5 and 7 (i.e., the close price and the volume).

import numpy as np

apple = "/Users/polinaprinii/Downloads/AAPL.csv"

a, b = np.loadtxt(apple, delimiter=',', usecols=(4,6), unpack=True, skiprows=1)
# delimiter corresponds to how the columns are seperated, in this case CSV = comma seperated values
# usecols corresponds to which columns we want, 4 = to Close and 6 = Volume. REMEMBER indexing starts at 0 in python.
# unpack = True allows for the data to be displayed in a vector.
# skiprows = 1 skips the header rows otherwise its defaulted to 0 and only used when the first row in the file is of int data type.

print("Close data is as follows: ", "\n", a, "\n", "\n", "Volume data is as followes: ", "\n", b)
#Note that the above array is assigned to multiple variable in this case a and b. a pulls the Close data idenitfied as column 4 and b pull Volume from column 6.


# In[98]:


# 2) Based on the data provided, calculate the volume weighted average price for the stock 
#(i.e., calculate the average price using the volume as weight values).

print("The Average is volume weighted is: ", np.average(a, weights=b)) #a is the Close data and b is the Volume data which we use for weight.


# In[99]:


#3) Calculate the median value of the closing prices (hint: use the median function).

print("The median for closing prices is: ", np.median(a)) 


# In[100]:


#4) Calculate the variance value of the closing prices.

print("The variance value of closing prices is: ", np.var(a))


# In[106]:


#5) Again, use the loadtxt command to load data from columns 3 and 4 (i.e., the high prices and the low prices).

c, d = np.loadtxt("/Users/polinaprinii/Downloads/AAPL.csv", delimiter=',', usecols=(2,3), unpack=True, skiprows=1)

print("High Prices data is as follows: ", "\n", c, "\n", "\n", "Low Prices data is as follows: ", "\n", d)


# In[111]:


#6) Use the max and min functions to get the highest high and the lowest low value.

print("The highest high value is: ", "\n", np.max(c), "\n")

print("The lowest low value is: ", "\n", np.min(d))


# In[116]:


#7) Load data from column 5 of AAPL.csv. Also, load data from column 5 of MSFT.csv.

apple_data = "/Users/polinaprinii/Downloads/AAPL.csv"
microsoft_data = "/Users/polinaprinii/Downloads/MSFT.csv"

aapl = np.loadtxt(apple_data, delimiter=',', usecols=(4), unpack=True, skiprows=1)
msft = np.loadtxt(microsoft_data, delimiter=',', usecols=(4), unpack=True, skiprows=1)

print("Apple data for Column 5 is: ", "\n", aapl, "\n")
print("Microsoft data for column 5 is: ", "\n", msft, "\n")


# In[122]:


#8) Calculate the covariance matrix of the closing prices of AAPL and MSFT (hint: use the cov function).

cov = np.cov(aapl, msft)
print("The covariance matrix of the closing prices for AAPLE and MSFT is: ", "\n", cov)


# In[123]:


#9) View the values on the diagonal (hint: diagonal).

dia = cov.diagonal()
print("Values on the diagonal: " , "\n", dia)


# In[125]:


#10) Calculate the correlation coefficient of the closing prices of AAPL and MSFT (hint:corrcoef).

corr = np.corrcoef(aapl, msft)
print("The correlation coefficient of the closing prices of AAPL and MSFT is: ", "\n", corr)


# In[128]:


# Regular Expresssions Exercise

#1) Write a Python program that will identify URLs using regular expressions.

import re
text = """Here are some URL's: 
            1st) Facebook URL: "https://www.facebook.com"
            2nd) Google URL: "https://www.google.com/?client=safari"
            3rd) National College of Ireland URL: "https://www.ncirl.ie"
            """
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Urls: ",urls)


# In[130]:


#Text Analytics Exercise

#1) Complete the tutorial at https://data-flair.training/blogs/nltk-python-tutorial/


# In[ ]:




