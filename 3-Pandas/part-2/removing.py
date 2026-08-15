# Drop method is used to delete any row or column
import pandas as pd
data = {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','jagdish','karan','prena'],
    "Age": [28,None,27,40,39,43,34,30],
    "Salary": [50000,60000,55000,52000,49000,70000,48000,80600],
    "Performance_Score" : [85,90,78,91,88,95,80,89]
}

df = pd.DataFrame(data)


# df.drop(columns = ["columnName"], inplace= True)

# for single column removing 

# df.drop(columns=['Performance_Score'], inplace=True)

# for multiple columns removing 
# df.drop(columns=['Performance_Score', 'Age'], inplace=True)
# df.dropna(subset=['Age'],inplace=True)

print(df)