# Raw data ko summarize karke useful information nikalna = Aggregation.

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

#==============================================

# summary statistic 
# df['columnName'].mean()
# df['columnName'].sum()
# df['columnName'].min/max()
# df['columnName'].count()

avg_marks = df['Marks'].mean()
sum = df['Marks'].sum()
count = df["Marks"].count()

print(avg_marks)
print(sum)
print(count)
