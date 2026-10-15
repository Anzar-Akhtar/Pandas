import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [92, 95, 88, 90, 97]
})

# Ques1:- Find the sum of marks
total_marks = students["Marks"].sum()
print(total_marks)

# Ques2:- Find the Average marks
avg_marks = students["Marks"].mean()
print(avg_marks)

# Ques3:- Find the max, min, median of the marks
print("Maximum Marks: ", students["Marks"].max())
print("Minimum Marks: ", students["Marks"].min())
print("Median Marks: ", students["Marks"].median())

# Ques4:- Count the Non-Missing Values
count_marks = students["Marks"].count()
print(count_marks)

# Ques5:- Calculate mean, minimum, maximum and sum using agg()
result = students["Marks"].agg(
    ["mean", "max", "min", "sum"]
)
print(result)


df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Salary": [50000, 60000, 40000, 45000, 55000, 65000],
    "Experience": [2, 4, 1, 3, 3, 5]
})
print("Overall Average Salary: ", df["Salary"].mean())
print("Highest Salary: ", df["Salary"].max())
print("Lowest Salary: ", df["Salary"].min())

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())

print("\nDepartment-wise Average Experience")
print(df.groupby("Department")["Experience"].mean())