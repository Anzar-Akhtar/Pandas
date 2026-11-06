import pandas as pd


# pd.concat() – DataFrames ko combine karna
df1 = pd.DataFrame({
    "Name": ["Alex", "John"],
    "Marks": [85, 90]
})

df2 = pd.DataFrame({
    "Name": ["Honey", "Chris"],
    "Marks": [88, 92]
})

result = pd.concat([df1, df2])
print(result)

result2 = pd.concat([df1, df2], ignore_index=True)
print(result2)

# pd.merge() – Common column ke basis par combine
students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Alex", "John", "Honey", "Chris"]
})

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105],
    "Marks": [85, 90, 88, 75]
})
res = pd.merge(students, marks, on="Student_ID")
print(res)

# .join() – Index ke basis par combine
df3 = pd.DataFrame({
    "Name": ["Alex", "John", "Honey"]
}, index=[101, 102, 103])

df4 = pd.DataFrame({
    "Marks": [85, 90, 88]
}, index=[101, 102, 103])

res2 = df3.join(df4)
print(res2)