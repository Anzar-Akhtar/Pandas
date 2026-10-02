import pandas as pd
import numpy as np

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, np.nan, 22, 23],
    "Marks": [85, np.nan, 76, 88, 95],
    "Attendance": [92, 95, 88, np.nan, 97]
})

print(students)

# isnull():- if we want to check which values are missing
print(students.isnull())

# isnull().sum():- if we want to check how many values are missing in each column
print(students.isnull().sum())

# if we want to check which values are missing in a specific column
print(students["Marks"].isnull())

# notnull():- if we want to check which values are not missing
print(students.notnull())

# dropna():- if we want to drop the rows which have missing values
print(students.dropna())

# fillna():- if we want to fill the missing values with a specific value
print(students.fillna(0))

# fill the value with the mean of the column
print(students["Marks"].fillna(
    students["Marks"].mean())
)