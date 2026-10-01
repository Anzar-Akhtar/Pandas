import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [92, 95, 88, 90, 97]
})

# print(students)

# Adding new cloumns to the DataFrame
students["Passed"] = students["Marks"] >= 45
# print(students)

students["Country"] = "India"
print(students)

# Existing column se new column create karna
students["Bonus"] = students["Marks"] + 5
print(students)

# Multiple Columns Se New Column
students["Performance"] = (
    students["Marks"] + students["Attendance"]
) / 2
print(students)

# Column rename karna
students.rename(
    columns={"Marks": "Score"},
    inplace=True
)
print(students)

# column delete karna
students.drop(
    columns=["Age"],
    inplace=True
)
print(students)