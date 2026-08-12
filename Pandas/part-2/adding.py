# 1- how to add column 
# 2- how to remove column 
# 3- how to update column 

# --------------------------------------------------------------------------------------------

import pandas as pd
data = {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
    "Age": [28,33,27,40,39,43,34,30],
    "Salary": [50000,60000,55000,52000,49000,70000,48000,80600],
    "Performance_Score" : [85,90,78,91,88,95,80,89]
}
df = pd.DataFrame(data)

# use a square bracketss df["column_name"] = some_Data  -> add column at the last 

# df["Bonus"]  = df['Salary'] * 0.1 

# using insert method -> you can add new column at specific position or index in data frame   
# df.insert(loc, "column_Name, some_data")

df.insert(0, "Employ Id", [10,20,30,40,50,60,70,80])



print(df)