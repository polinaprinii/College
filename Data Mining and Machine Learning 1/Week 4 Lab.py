"""
Numerical Analysis Exercises Pandas – Shark Attack Dataset:
For each of the following questions you will use a dataset containing information on global shark attacks called attacks.csv.
Attribute Information:
The attributes recorded in the dataset are as follows: 1. Case Number
2. Date
3. Year
4. Type
5. Country
6. Area
7. Location
8. Activity
9. Name
10. Sex
11. Age
12. Injury
13. Fatal
14. Time
15. Species
16. Investigator or Source
Open this file using Pandas read_csv() function. The data file is stored in a different encoding format so you can use the following line to read the data into a dataframe.
df = pd.read_csv('attacks.csv', encoding = "ISO-8859-1")
"""

import pandas as pd
"""
(i)
What location globally has the highest number of shark attacks?
"""
# Importing file to pandas.
df = pd.read_csv('/Users/polinaprinii/Downloads/Lab -- attacks.csv', encoding = "ISO-8859-1")
#print(df)

# Checking data types of each column.
#print(df.dtypes)

# Grouping data by Country to determine the location.
df_group = df.groupby('Country')['Case Number'].nunique().nlargest(1)
print("The top location globally is: ", df_group, "\n")

"""
(ii)
Read the shark attack dataset into a Pandas Dataframe.
Determine the six countries that have experienced the highest number of shark attacks.
"""
# Determining top 6 countries with most attacks.
df_top6 = df.groupby('Country')['Case Number'].nunique().nlargest(6)
print("The top six countries are as below: ", "\n", df_top6, "\n")

"""
(iii)
Modify your code to print out the six countries that have experienced the highest number of fatal shark attacks.
"""
# Determining top 6 countries with most fatal attacks.
df_top_fatal = df.groupby('Country')['Fatal'].nunique().nlargest(6)
print("The top six countries with the most fatal attacks are as below:", "\n", df_top_fatal, "\n")

"""
(iv)
Based on the data in the Activity column are you more likely to be attacked by a shark if you are 
“Surfing” or “Scuba Diving”
"""
surfing = df['Activity'].value_counts()['Surfing']
scuba = df['Activity'].value_counts()['Scuba diving']
print("Based on the data provided it is more like for a shark attack to occur whilst surfing with a total of:",
      surfing,"attacks, against scuba diving with a total of:", scuba, "\n")

"""
(v)
Determine from the dataset what percentage of all recorded shark attacks were fatal.
"""
total_cases = df['Case Number'].count()
total_fatal_cases = df['Fatal'].value_counts()['Y']
print("The percentage of fatal attack are:", round((total_fatal_cases/total_cases) * 100), "%")

"""
(vi)
For each individual country, print out the percentage of fatal shark attacks 
(number of fatal shark attacks expressed as a percentage of the total number of shark attacks). 
Some countries have recorded 0 fatal and non-fatal attacks. 
Your code should only consider countries where the number of non-fatal and fatal attacks are greater than 0.
"""
group1 = df.groupby('Country')['Fatal'].value_counts()
print(group1)

for index, value in group1.items():
    if index[1] == 'Y':
        print("Country ",index[0], "has a total percentage of fatal cases against world total of:", (value/total_fatal_cases) * 100, "%")

