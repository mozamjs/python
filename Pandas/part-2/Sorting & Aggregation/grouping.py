


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
    "Salary": [
        50000, 60000, 45000, 52000, 64000, 58000, 34000, 45000, 85000, 40000
    ]
}

df = pd.DataFrame(data)

grouped = df.groupby('Age')['Salary'].sum()

print(grouped) 