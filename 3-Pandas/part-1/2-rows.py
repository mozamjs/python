#Previewing the Data

#  head() tail()
# head() => 5 row from start will show if no number is given 


import pandas as pd

df = pd.read_json("sample_Data.json")

print('display 10 rows of first')
print(df.head(10))

print('display 10 rows of Last')
print(df.tail(10))