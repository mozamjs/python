# interpolation is a technique uused to fill astimated value  at missing place -> just use for numarical column   

# linear interpolation 
# polinomial interpolation 

# 1- preserve data integrity (missing values is replaced with arbity number  (predict number0))
# 2- Smooth trends
# 3- avoid data loss(instad of deleting or filling missing data with default value fill with astimated value ) avoid dropping rows 

# interpolate()

# linear, ploynomial, time 
# df.interpolate(method="linear", axis=0, inplace=True )

# --------------------------------------------------------



import pandas as pd

data= {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}


df = pd.DataFrame(data)
print('Before interpolation')
print(df)

# df['Value'] = df['Value'].interpolate(method = 'linear')
# df['Value'] = df['Value'].interpolate(method = 'polynomial', order = 2)

print('After interpolation')
print(df)