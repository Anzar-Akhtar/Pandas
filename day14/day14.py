import pandas as pd

data = pd.DataFrame({
    "Name": ["Alex", "John", "Honey", "Chris", "Sam", "Peter", "Riya", "Ankit"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "Sales", "Sales", "HR"],
    "Gender": ["Male", "Male", "Female", "Male", "Male", "Male", "Female", "Male"],
    "Salary": [50000, 40000, 60000, 45000, 55000, 35000, 42000, 48000],
    "Experience": [3, 2, 5, 2, 4, 1, 3, 4]
})

# print(data)

# groupby():-Maan lo tumhe har department ki average salary calculate karni hai.

res = data.groupby("Department")["Salary"].mean()
# print(res)

# agg() – Multiple calculations at once
res2 = data.groupby("Department")["Salary"].agg(
    ["mean", "max", "min", "sum"]
)
# print(res2)

res3 = data.groupby("Department").agg({
    "Salary": ["mean", "max"],
    "Experience": ["mean", "max"],
    "Name": "count"
})
# print(res3)

# value_counts() – Frequency count karna
# print(data["Department"].value_counts())

# pivot_table() – Summary table banana
res4 = pd.pivot_table(
    data,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
# print(res4)

# apply() – Custom operations perform karna
def salary_category(salary):
    if salary >= 50000:
        return "High Salary"
    else:
        return "Normal Salary"

data["Salary_Category"] = data["Salary"].apply(salary_category)
print(data[["Name", "Salary", "Salary_Category"]])