import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [92, 95, 88, 90, 97]
})

# print(students)

# Question1:- add the passed column to the DataFrame
students["Passed"] = students["Marks"] >= 45
# print(students)

# Question2:- Add the bonus column
students["Bonus"] = students["Marks"] + 5
# print(students)

# Question3:- Add the performance column in which calculate average using marks & attendance
students["Performance"] = (
    students["Marks"] + students["Attendance"]
) / 2
# print(students)

# Question4:- Renaming
students.rename(
    columns = {"Name": "Student_Name", "Marks": "Score"},
    inplace=True
)
print(students)