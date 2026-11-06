import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Alex", "John"],
    "Marks": [85, 90]
})

df2 = pd.DataFrame({
    "Name": ["Honey", "Chris"],
    "Marks": [88, 92]
})

# Ques1:- combine two dataframe vertically
result = pd.concat([df1, df2])
print(result)

# Q2. Combine two DataFrames horizontally using axis=1
result2 = pd.concat([df1, df2], axis=1)
print(result2)

# Q3. Combine two DataFrames and reset the index
result3 = pd.concat(
    [df1, df2],
    ignore_index=True
)
print(result3)

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Alex", "John", "Honey", "Chris"],
    "Department": ["AI", "Cloud", "AI", "Cloud"]
})

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105],
    "Marks": [85, 90, 88, 75]
})

# Q4. Merge students and marks using Student_ID
result4 = pd.merge(
    students,
    marks,
    on="Student_ID"
)
print(result4)