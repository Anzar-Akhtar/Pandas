import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [92, 95, 88, 90, 97]
})

df = students

# Question1:- sort the marks in ascending order
print(df.sort_values("Marks"))

# Question2:- sort the marks in descending order
print(df.sort_values("Marks", ascending=False))

# Question3:- Arrange the age in ascending order and then marks in descending order
print(df.sort_values(["Age", "Marks"], ascending=[True, False]))

# Question4:- give the ranks according to the marks
df["Rank"] = df["Marks"].rank(ascending=False, method="average")
print(df[["Name", "Marks", "Rank"]])

# Question5:- sort index in descending order
print(df.sort_index(ascending=False))