import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris",
             "Rahul", "Priya", "Aman", "Neha", "Arjun"],
    "Age": [20, 21, 20, 22, 23, 21, 20, 22, 21, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA",
               "BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95, 68, 91, 73, 89, 64],
    "Attendance": [92, 95, 88, 90, 97, 82, 94, 85, 91, 78]
})

print(students)

print(students[students["Marks"] > 80])
print(students[students["Marks"] > 80][["Name", "Marks"]])
print(students[students["Marks"] > 80][["Name", "Attendance"]])

print(
    students[
        (students["Marks"] > 80) &
        (students["Attendance"] > 90)
    ]
)

print(
    students[
        (students["Marks"] >= 90) |
        (students["Attendance"] >= 95)
    ]
)

print(
    students[
        ~(students["Marks"] > 80)
    ]
)

# isin
print(
    students[
        students["Age"].isin([20,22])
    ]
)