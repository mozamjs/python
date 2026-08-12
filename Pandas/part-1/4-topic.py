""" 1- how big is your data set 
 2- what are the names of the columns

 shape => Tell us how many rows and columns in our data set (attribute)
 column => Return the name of column as an index object   and also if you want to change the name of column u should do  (attribute)
"""

import pandas as pd 


# data = {
#     "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
#     "Age": [28,33,27,40,39,43,34,30],
#     "Salary": [50000,60000,45000,52000,49000,70000,48000,80600],
#     "Performance Score" : [85,90,78,91,88,95,80,89]
# }

# df = pd.DataFrame(data)

df = pd.read_json("./sample_Data.json")
print(df)
print(f'shape: {df.shape}')
print(f"Column Names: {df.columns}")
