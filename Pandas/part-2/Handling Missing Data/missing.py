

# print(df.isnull())
# print(df.isnull().sum())

# dropna()
# df.dropna(axis = 0(row ma jo missing value ha us ko urana) / axis = 1 (column ma jo missing value ha us ko uran) , inplace = True)

# fillna()
# fillna(value, inplace= True)

# -------------------------------------------------------------------------------------------------

import pandas as pd

data = {
    "Name": ['Ram',None,'Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
    "Age": [28,None,27,40,39,43,34,30],
    "Salary": [50000,None,55000,52000,49000,70000,48000,80600],
    "Performance_Score" : [85,None,78,91,88,95,80,89]
}
df = pd.DataFrame(data)
# df = df.astype(object)

# df.dropna(inplace=True)

# df.fillna(0, inplace=True)

# df['Age'] = df['Age'].fillna(df['Age'].mean(), inplace=True)
# df.fillna({'Age':0}, inplace=True)
# df.fillna({'Age':df['Age'].mean()}, inplace=True)

print(df)