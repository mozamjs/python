# import pandas as pd

# print(pd. __version__)

# mydataset={
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3,7,2]
# }

# myvar = pd.DataFrame(mydataset)
# print(myvar)


# read data from a CSV file into a dataframe 
# encoding = "utf-8"   /    encoding = 'latin1'   these two are formate to read files if error comes 
# gcsfs use to read the data of claude plateform  

# import pandas as pd 
# df = pd.read_csv("sales_data_sample.csv")

# df = pd.read_excel("sales_data_sample.xlsx")
# print(df)

# df = pd.read_json("sample_Data.json")
# print(df)

import pandas as pd
df = pd.read_csv("data.csv")
print(df)