
# .loc[] is a method in pandas which is use to access or update specfic row or column  or set of rows and columns

# import pandas as pd
# data = {
#     "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
#     "Age": [28,33,27,40,39,43,34,30],
#     "Salary": [50000,60000,55000,52000,49000,70000,48000,80600],
#     "Performance_Score" : [85,90,78,91,88,95,80,89]
# }

# df = pd.DataFrame(data)

# .loc[] 
# df.loc[row_index, "column Name"] =new_value


# df.loc[0,"Salary"] = 65000

# print(df)


# if you want to update multiple rows and columns

import pandas as pd
data = {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
    "Age": [28,33,27,40,39,43,34,30],
    "Salary": [50000,60000,55000,52000,49000,70000,48000,80600],
    "Performance_Score" : [85,90,78,91,88,95,80,89]
}

df = pd.DataFrame(data)

df['Salary'] = df['Salary'] * 1.05

print(df)







