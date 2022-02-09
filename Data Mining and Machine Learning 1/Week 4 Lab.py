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
# """
# (i)
# What location globally has the highest number of shark attacks?
# """
# # Importing file to pandas.
# df = pd.read_csv('/Users/polinaprinii/Downloads/Lab -- attacks.csv', encoding = "ISO-8859-1")
# print(df)
#
# # Checking data types of each column.
# print(df.dtypes)
#
# # Grouping data by Country to determine the location.
#
# df_group = df.groupby('Country')['Case Number'].nlargest(6)
#
# print(df_group)