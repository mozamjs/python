# sorting data

import pandas as pd

data = {
    "Name": [
        "Ali", "Mozam", "Sara", "Bilal", "Ayesha",
        "Usman", "Zainab", "Danish", "Hira", "Ahmed"
    ],
    "Age": [
        21, 19, 22, 20, 18,
        23, 20, 21, 19, 22
    ],
    "Marks": [
        78, 99, 65, 85, 95,
        72, 88, 60, 91, 80
    ]
}

df = pd.DataFrame(data)


# sorting data in 1 column 
# df.sort_values(by= "column Name ", ascending= True/False, inplace = True )



# df.sort_values('Marks',ascending=False,inplace= True)
df.sort_values(by=['Marks', 'Age'], ascending = [False,False], inplace=True)
print(df)