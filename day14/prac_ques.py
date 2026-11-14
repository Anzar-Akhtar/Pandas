import pandas as pd

data = pd.DataFrame({
    "Name": ["Alex", "John", "Honey", "Chris", "Sam", "Peter", "Riya", "Ankit"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "Sales", "Sales", "HR"],
    "Gender": ["Male", "Male", "Female", "Male", "Male", "Male", "Female", "Male"],
    "Salary": [50000, 40000, 60000, 45000, 55000, 35000, 42000, 48000],
    "Experience": [3, 2, 5, 2, 4, 1, 3, 4]
})

# 1. Avg salary by department
print("\nAverage Salary:")
print(data.groupby("Department")["Salary"].mean())

# 2. Multiple salary calculations
print("\nSalary Analysis:")
print(data.groupby("Department")["Salary"].agg(
    ["mean", "max", "min", "sum"]
))

# 3. Gender distribution
print("\nGender Distribution:")
print(data["Gender"].value_counts())

# 4. Employee count by department
print("\nEmployee Count:")
print(data["Department"].value_counts())

# 5. Pivot Table
print("\nDepartment and Gender Analysis:")
print(pd.pivot_table(
    data,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean",
    fill_value=0
))

# 6. Create salary category
data["Salary_Category"] = data["Salary"].apply(
    lambda x: "High" if x >= 50000 else "Normal"
)

# 7. Display highest salary employees
print("\nHighest Salary Employees:")
print(data[data["Salary"] == data["Salary"].max()])

# 8. Final dataset
print("\nFinal Dataset:")
print(data)