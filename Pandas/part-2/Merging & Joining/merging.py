# when we want to work on more then one data set so merging concept comes 

# 2 ya 2 sa zyada dataframe ki rows ko combine karna based on a common key column like sql joins two tables

# pd.merge(df1, df2, on='column_name(which are same in both df)', how = "type of join ")
# cross, inner, outer, left, right 

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import pandas as pd

customer = {
    'CustomerID' : [1,2,3],
    'Name': ['Ramesh','Suresh', 'kalpesh']
}

order = {
    'CustomerID': [1,2,4],
    'OrderAmount': [250,450,350]
}

df_customers = pd.DataFrame(customer)
df_order = pd.DataFrame(order)

# .................................................

# df_merged = pd.merge(df_customers,df_order, on = 'CustomerID',how="inner")

# print("inner join ")
# print(df_merged)

# .................................................

# df_merged = pd.merge(df_customers,df_order, on = 'CustomerID',how="outer")

# print("outer join ")
# print(df_merged)

# .................................................

df_merged = pd.merge(df_customers,df_order, on = 'CustomerID',how="left")

print("Left join ")
print(df_merged)

# .................................................

df_merged = pd.merge(df_customers,df_order, on = 'CustomerID',how="right")

print("right join ")
print(df_merged)

# .................................................

df_merged = pd.merge(df_customers,df_order, how="cross")

print("cross join ")
print(df_merged)


# print(df_customers)
# print(df_order)