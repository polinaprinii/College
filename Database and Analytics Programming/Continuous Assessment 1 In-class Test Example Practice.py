#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[2]:


# Here we import all packages as needed.
import xml.etree.ElementTree as ET


# Question 1(a):

try:
    file = "/Users/polinaprinii/Documents/Database & Analytics Programming/covid.xml" # Here we declare a var which holds our file location for the xml file.
    tree = ET.parse(file) # Parsing means to read information from a file and split it into pieces by identifying parts of that particular XML file. The tree variable is holding our file location as well as structure of the file. 
                            

except FileNotFoundError as error: # In the case the file path is specified incorrectly
    print('Something went wrong.') # Easy to understand error
    print('Error: ', error) # Display the error type and the file path.
    
else: # else defines a block of code to be executed if no errors were raised
    root = tree.getroot() # obtaining the root of the XML tree.
    print('Root of XML is: ', root, '\n')
    

finally: 
    print('You have finished Question 1 (a)')


# In[3]:


for child in root[0]: #Enquire with Rashid why the attributes are not coming through.
    print(child.tag, child.attrib)


# In[4]:


# 1(b)
# Write code to print a list of all the tags of the first record of the xml tree above.

tags = [] # Create a list which will hold our tags
for child in root[0]: # a loop which looks for all the tags in the first record identified as 0 due to the indexing nature of python
    tags.append(child.tag) #add (append) all the identified tags within the first record to our tags list
print(tags) #display/print our tags list. 


# In[5]:


# 1(c)
# Write code to print records from the xml including the day, month, year, cases, deaths and Cumulative_number_for_14_days_of_COVID-19_cases_per_100000 for Ireland for October 2020.

values = {} #Creating a dictionary to hold our desired values
for covid_record in root.findall('record'): #1st loop scans the document for all record cellls
    values = {tag: covid_record.find(tag).text for tag in tags} #2nd loop is to identify each tag for every covid_record created within the dictionary and derive the text.
    if values['countriesAndTerritories'] == 'Ireland' and values['month'] == '10' and values['year'] == '2021':
        print(values['day'], values['month'], values['year'], values['cases'], values['deaths'])


# In[6]:


# 1(d)
#Extract the above XML data and write it to a CSV file. Your file should also contain the column names.

import pandas as pd #Python package which works with CSV files.

cols = ["day", "month", "year", "cases", "deaths"] #Specify the columns which will hold the above data as well as name the columns.
rows = [] #We keep rows empty as the above data will be used to populate.

for covid_record in root.findall('record'):
    values = {tag: covid_record.find(tag).text for tag in tags}
    if values['countriesAndTerritories'] == 'Ireland' and values['month'] == '10' and values['year'] == '2021':
        rows.append({'day': values['day'],
                    'month': values['month'],
                    'year': values['year'],
                    'cases': values['cases'],
                    'deaths': values['deaths']})
#For the above we re-use the code for the two loops and if statements.
#Using the append() function we populate the rows according to the columns and the values dictionary.
    
df = pd.DataFrame(rows, columns=cols) #we define our panda dataframe which will convert our XML to CSV.
  
# Writing dataframe to csv and specifying the location to 
df.to_csv("/Users/polinaprinii/Documents/Database & Analytics Programming/output.csv")


# In[1]:


# Question 2

# 2(a) - removing lowercase substrings from the string

import re # Accessing regular expression operations which allows us to work with our string.

remove_lowercase = lambda string_text: re.sub('[a-z]', '', string_text) # we create a variable which will hold our lamba function results
# Above we declare the lambda by the name string_text to use the re.sub function which used to replace occurrences of a particular sub-string with another sub-string.
# In the [] we declare that we want anything from lower a to lower z to be replaced with nothing by using empty ''.

my_string = 'H9eoDAPklo-oPGserfDDAoa_SEPiskdsf' # We declare our string.
my_string = remove_lowercase(my_string) # using our previously outline variable we apply the lambda function to our delcared string.

print(my_string)


# In[2]:


# 2(b) - using regular expression to identify all the URLs in the text, and return them as an array.

# Using the regular expression import from above we do the following:

url_string = """<p>College Website :</p><a href="https://www.ncirl.ie/">National College of Ireland</a><p>Course
Website :</p><a href="https://mymoodle.ncirl.ie/course/view.php?id=633">PGGDA_SEP H9DAP</a>""" # Using triple " as there are "" used within the string itself.


def Find(url_string): # Defining a function which will look for our URL's
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,url_string) # using the findall() function we use regex and go through our string to find matching values      
    return [x[0] for x in url] # In our return statement, we create an array identified as x and filter the url variable using a loop to populate the array.
print("Urls: ", Find(url_string))


# In[7]:


# 2(c) - Write a regular function that highlights the occurrence of any of the strings Python, you and program.

# Using the regular expression import from 2(a)
import re

providedText = '''Python is a programming language.
Python lets you work more quickly and integrate your systems more effectively. 
Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages.
Python is developed under an OSI-approved open source license, making it freely usable and distributable, even for commercial use.
The Python Package Index (PyPI) hosts thousands of third-party modules for Python.'''

pat = r"Python|you|program" #Using the re package we define the criteria we are looking to match denoted by r""

def re_show(x, y): #We build a function to highlight our desired criteria. x and y are classified as parameters which are specified below.
    print("Our text is highlighted as follows:", "\n", "\n", re.sub(x, "*\g<0>*", y)) # The re.sub() will scan through our y parameter which is our provided text and replace all matching values to place a * at the start and end of the word.
# \g<0> in regex Inserts the entire match. Ultimetely we add the * to highlight the word.
re_show(pat, providedText) #Here we specify the parameters for our function.


# In[1]:


# Question 3

# 3(a) - Create a 7x5 integer array from a range between 100 to 450 such that the difference between each element is 10 and then split the array into five equal-sized sub-arrays

import numpy as np # We import the library consisting of multidimensional array objects and a collection of routines for processing of array.

a1 = np.arange(100, 450, 10)
print(a1, "\n")

a2 = a1.reshape(7, 5)
print(a2, "\n")

a3 = np.split(a1, 5)
print(a3)

#Note you can arrange and reshape in one line by typing np.arrange(-, -, -).reshape(-, -). However, when splitting the array it posses problems.


# In[40]:


# 3(b) - Write a function to return an array of odd rows and even columns
import numpy as np

ar1 = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

print(ar1, "\n")

def odd_even(x):
    x = x[::2, 1::2]
    print(x)
    
odd_even(ar1)


# In[47]:


# 3(c) - Print the maximum value in each row.
import numpy as np

ar2 = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(ar2, "\n")

maxValue = numpy.amax(ar2, axis=1)
print(maxValue)


# In[ ]:




