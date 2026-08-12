# 1- Select specific column -> (use square brackets to select specific column)
# 2- filter rows -> (boolean conditions )
# 3- combine multiple conditions 

# Selecting columns
# 1- a series
# 2- dataframe multiple columns of data 

# column = df["column Name"]
# subset = df = ["column1", "column2",]



# filtering rows
# boolean indexing 

# based on a single condition 

# filtered_Rows = df[df['column_Name'] > 50000]

# combine multiple condition

# filtered_Rows = df[(df['column_Name'] > 50000) & (df['column2'] < 80000) ]



#-----------------------------------------------------------------------------------------------

import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
    "Age": [28,33,27,40,39,43,34,30],
    "Salary": [50000,60000,55000,52000,49000,70000,48000,80600],
    "Performance_Score" : [85,90,78,91,88,95,80,89]
}

df = pd.DataFrame(data)


# print("sample DataFrame..")
# print(df)

# print("Names (single column return series)")
# name = df['Name']
# print(name)

# selecting multiple columns 
# subset = df[['Name','Salary']]
# print('\n Subset with Name and Salary')
# print(subset)

# filtering rows based on single condition 

# high_salary = df[df['Salary'] > 50000]
# print('Employees with salary > 50000')
# # print(high_salary["Name"])
# print(high_salary)

# filtering rows with multiple conditions 

# filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
filtered = df[(df['Age'] > 30) | (df['Performance_Score'] > 90)]

print(filtered)
