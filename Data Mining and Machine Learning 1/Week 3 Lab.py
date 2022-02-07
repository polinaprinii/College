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


def raindays():
    x = input("Please input year for which we will retrieve the sum of Rainy Days: ")
    cork_rainy_days = cork_data[:,0] == int(x)
    sum_rainy_days = np.sum(cork_data[cork_rainy_days][:,4])
    print("The total Rain Days for ", x, "is ", sum_rainy_days, "\n")

#raindays()

"""
(iii) Calculate the wettest month of the year in Cork based on the “Total Rainfall” value. 
The month that has the highest cumulative “Total Rainfall” value across all years should be classified as the wettest. 
Your code should print out the month and the cumulative total rainfall value for that month.
"""
import calendar
def rainfall():
    wettest_month = cork_data[cork_data[:, 2] == np.max(cork_data[:, 2])]
    print("The wettest month within out data set happened in", calendar.month_name[int(wettest_month[: ,1])], ":",
          int(wettest_month[:, 0]), "with a value of:", int(wettest_month[:, 2]), "mm", "\n")
#rainfall()


"""
(iv) This question focuses on the Number of Rain days column. The user is asked to enter
a maximum threshold value for the number of rain days. Your code should then
output the percentage of the time (percentage of rows in the dataset) where the
number of rain days is less than or equal to the threshold value.For example, 
if a user enters a maximum threshold value of 6, then your code should
output the percentage of rows where the number of rain days fell between the threshold value of 6.
"""

def countrainydays():
    no_rain_days = input("Please enter a threshold for which we'd like to find the number of rain days: ")
    rain_day_arr = cork_data[:,[4]]
    count_arr = np.count_nonzero(rain_day_arr)
    count_occ = np.count_nonzero(rain_day_arr <= int(no_rain_days))

    print("The provided threshold of:", no_rain_days, "results in a", round((count_occ/count_arr) * 100),
          "% value from the overall row count.", "\n")

countrainydays()
