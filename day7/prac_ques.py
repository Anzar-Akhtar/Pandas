import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, np.nan, 22, 23],
    "Marks": [85, np.nan, 76, 88, 95],
    "Attendance": [92, 95, 88, np.nan, 97]
})
df = students
print(df)
print()

# Question1:- check the missing values
print(df.isnull())

# Question2:- Find the count of the missing values
print(df.isnull().sum())

# Question3:- find only those students whose marks is missing
print(
    df[
        df["Marks"].isnull()
    ]
)

# Question4:- find those students whose marks is not missing
print(
    df[
        df["Marks"].notnull()
    ]
)

# Question5:- Remove Missing rows
print(df.dropna())

# Question6:- Remove only the marks missing rows
print(
    df.dropna(subset=["Marks"])
)

# Question7:- fill the missing marks value with 0
df["Marks"] = df["Marks"].fillna(0)
print(df)

# Question8:- fill the marks missing value with the help of mean
print(
    df["Marks"].fillna(df["Marks"].mean())
)