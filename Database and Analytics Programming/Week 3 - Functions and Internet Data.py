#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[1]:


#Week 3 Lab

#Question 1:
def mul_by_num(num):
    return (lambda x: x*num)

#here we are assigning value to num from our function
x = mul_by_num(5)
y = mul_by_num(2)

#here we are assigning a value to the x from the lambda function
print(x(3))
print(y(-4))


# In[3]:


#Question 2:

# Function for nth Fibonacci number
def Fibonacci(n):
   
    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return lambda a, b: a(Fibonacci(n-1)) + Fibonacci(n-2)
 

    print(Fibonacci(20))


# In[4]:


#Question 2 - def Function

def fibonacci_of(n):
    if n in {0, 1}:  # Here we define our dictionary for n
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


[fibonacci_of(n) for n in range(5)]


# In[5]:


#Question 2 - lambda Function

from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], #an _ in lamba is an unamed variable which will always
                       #return True for the argument passed # [-1](last) & [-2](second last) returns the last numbers from the list at the point of index and adds them together
                       range(n-2), [0, 1]) #n-2 reduces the number of iterations by 2 which allows Python to print the desired number of items within the list rather than adding them to the list
                                            #in simpler terms -2 is specified as there are already 2 numbers in the list.
print(fib(5))


# In[6]:


#Question 3 Requesting API's

import requests

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Galway&appid=8f7bc5f03eafdc75c66b3a042a967262")

data = response.json()

#Temperature var
temp = data['main']['temp']
Kelvin_to_Celcius = temp - 273.15

#Wind var
wind = data['wind']['speed']

#Description var
description = [i ['description']for i in data['weather']] #because weather is an array, we are looping through it by looking for i which is description in this case

#Weather Var
weather = [i ['main']for i in data['weather']]


print('The current temperature is: ', str(round(Kelvin_to_Celcius, 2)),u'\N{DEGREE SIGN}C')
print('The wind speed is: ', wind, 'm/s')
print('Description: ', ", ".join(description)) #removes the [] from the list and joins all the items in the list.
print('Weather is: ', ", ".join(weather))


# In[9]:


#Question 4

import xml.etree.ElementTree as ET

tree = ET.parse('/Users/polinaprinii/Downloads/people.xml')

root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)


# In[1]:


#Question 4 Exporting to CSV

import xml.etree.ElementTree as ET
import pandas as pd
  
cols = ["Name", "Phone", "Email", "Address"]
rows = []

xmlparse = ET.parse('/Users/polinaprinii/Downloads/people.xml')
root = xmlparse.getroot()
    
for i in root: #A for in loop which will scan through the XML file pilling the information needed through the .find () function.
    Name = i.find("Name").text
    Phone = i.find("PhoneNumber").text
    Email = i.find("EmailAddress").text
    
    
    for x in root.iter("Address"): #A second for in loop in required due the Address tag being a nested child.
        Street = x.find("StreetLine1").text
        City = x.find("City").text
        State = x.find("StateCode").text
        PostalCode = x.find("PostalCode").text
        Address = Street + ',' + City + ',' + State + ',' + PostalCode
# The second loop pulls in information needed for the Address tag, at the end we declare a var which pull all the info into one record.    
    rows.append({'Name': Name,
                'Phone': Phone,
                'Email': Email,
                'Address': Address})
    
df = pd.DataFrame(rows, columns=cols) #We declare df as the dataframe of the to be csv file. 
print(df) # A good hack to see how your csv dataframe is coming out. 

df.to_csv("/Users/polinaprinii/Documents/Database & Analytics Programming/shouldwork.csv")
df.to_json("/Users/polinaprinii/Documents/Database & Analytics Programming/shouldwork.json")

