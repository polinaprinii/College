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
print("Based on the data provided", surfing, "\n", scuba)


"""
(v)
Determine from the dataset what percentage of all recorded shark attacks were fatal.
"""
df[df.columns['0']].count()