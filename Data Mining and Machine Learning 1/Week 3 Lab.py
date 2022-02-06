"""
The objective of the exercises is to familiarize yourself with the use of NumPy.
These excises are mainly based on rainfall data in Cork for each month over the past half century.
In the folder you will find a file called CorkRainfall.txt and a file called DublinRainfall.txt.
This is a space delimited file.
Each line of the file contains the following precipitation information pertaining to a specific month and year:
Year
Month (1 = Jan, 2 = Feb, 3 = March, etc. )  Total Rainfall (Millimetres)
Most Rainfall in a Day (Millimetres)
Rain days (0.2mm or More) (Number)

Please use NumPy to answer the following questions.
The objective of this task is to familiarize yourself with the operation of NumPy.
(There is no need to incorporate error checking).
"""

"""
(i) Print out the max ‘Most Rainfall in a Day’ value and the average ‘Most Rainfall in a Day’ value for the Cork data 
(That is, obtain the maximum value contained in this column of data and the average value in this column of data).
"""

import numpy as np

# Reading the Cork data using numpy.loadtxt
cork_data = np.loadtxt("/Users/polinaprinii/Downloads/CorkRainfall.txt", dtype = float)
# Performing a sanity check.
print(cork_data.shape, "\n")
print("Here is out Cork Rainfall data: ", "\n", cork_data, "\n")

# reading the Dublin data using numpy.loadtxt
dublin_data = np.loadtxt("/Users/polinaprinii/Downloads/DublinRainfall.txt", dtype = str)
# Performing a sanity check.
print("Here is our Dublin Rainfall data: ", "\n", dublin_data, "\n")

# We filter out Cork Rainfall data to a variable to only show the data for ‘Most Rainfall in a Day’, which is column 3.
cork_rain = cork_data[:, [3]]
# Finding the max ‘Most Rainfall in a Day’ for Cork.
print("The max ‘Most Rainfall in a Day’ in Cork recorded is: ", np.max(cork_rain), "\n")
# Finding the average ‘Most Rainfall in a Day’ for Cork.
print("The average ‘Most Rainfall in a Day’ in Cork recorded is: ", np.average(cork_rain), "\n")

"""
(ii) Display all unique years for which there is data in the dataset (you can use np.unique) 
Ask the user to select a specific year and output the total number of Rain Days per month for that year 
(that is, add up all the total number of Rain Days column for each month of that year).
"""
# Filtering numpy to only reflect 1st column aka [0] which contains Year information
unique_years = cork_data[:,[0]]
# Printing all unique years for which data was recorded. 
print("Here are all the years for which weather data was recorded for Cork city: ", "\n",
      np.unique(unique_years))

