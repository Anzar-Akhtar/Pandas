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

# print(students)


# Question1:- print the students whose marks is > 80
print(
    students[
        students["Marks"] > 80
    ]
)

# Question2:- print the students whose marks is >= 90
print(
    students[
        students["Marks"] >= 90
    ]
)

# Question3:- print only the name and marks whose marks > 80
print(
    students[
        students["Marks"] > 80] [["Name", "Marks"]
    ]
)

# Question4:- print the students whose marks > 80 and attendance > 90
print(
    students[
        (students["Marks"] > 80) &
        (students["Attendance"] > 90)
    ]
)

# Queation5:- print the students whose marks >= 90 or attendance >= 95
print(
    students[
        (students["Marks"] >= 90) |
        (students["Attendance"] >= 95)
    ]
)

# Question6:- use isin to selects only age
print(
    students[
        students["Age"].isin([20, 22])
    ]
)

# Question9:- AI/ML Practice
print(
    students[
        (students["Marks"] >= 85) &
        (students["Attendance"] >= 90) 
    ][["Name", "Age", "Attendance"]]
)