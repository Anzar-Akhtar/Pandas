import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [92, 95, 88, 90, 97]
})

# print(students)

# sum()
total_marks = students["Marks"].sum()
# print(total_marks)

# mean()
avg = students["Marks"].mean()
# print(avg)

# min()
minimum = students["Marks"].min()
# print(minimum)

# median()
median = students["Marks"].median()
# print(median)

# count()
count = students["Marks"].count()
# print(count)

# describe()
describe = (students["Marks"].describe())
# print(describe)

# agg() ka use multiple statistical operations ek saath karne ke liye hota hai.

result = students["Marks"].agg(
    ["mean", "min", "max", "sum"]
)
# print(result)

# multiple column statistics
result2 = students[["Marks", "Attendance"]].agg(
    ["mean", "min", "max"]
)
# print(result2)

# groupby():- divide the data according to the group
students2 = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris", "Rahul"],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA", "B.Tech"],
    "Marks": [85, 92, 76, 88, 95, 90],
    "Attendance": [92, 95, 88, 90, 97, 91]
})
df = students2
# print(df)

result3 = df.groupby("Course")["Marks"].mean()
# print(result3)

# groupby + sum
result4 = df.groupby("Course")["Marks"].sum()
# print(result4)

# groupby + multiple statistics
result5 = df.groupby("Course")["Marks"].agg(
    ["mean", "min", "max"]
)
# print(result5)

# multiple column + groupby
result6 = df.groupby("Course")[
    ["Marks", "Attendance"]
].mean()
print(result6)