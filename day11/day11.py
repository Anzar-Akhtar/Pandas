import pandas as pd

dates = pd.Series([
    "2026-01-15",
    "2026-02-20",
    "2026-03-25",
    "2026-04-10"
])

dates = pd.to_datetime(dates)

# print(dates)
# print(dates.dtype)

# Convert different data formats
dates2 = pd.to_datetime(
    dates,
    format="%D-%m-%Y"
)
# print(dates2)

employees = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Joining_Date": [
        "2023-01-15",
        "2022-06-20",
        "2024-03-10",
        "2021-12-05",
        "2023-08-25"
    ]
})

# Year, Month aur Day extract karna
employees["Joining_Date"] = pd.to_datetime(
    employees["Joining_Date"]
)

employees["Year"] = employees["Joining_Date"].dt.year
employees["Month"] = employees["Joining_Date"].dt.month
employees["Day"] = employees["Joining_Date"].dt.day

# print(employees)

# Month name aur day name extract karna
employees["Month_Name"] = (
    employees["Joining_Date"].dt.month_name()
)

employees["Day_Name"] = (
    employees["Joining_Date"].dt.day_name()
)

# print(employees[[
#     "Name", "Joining_Date", "Month_Name", "Day_Name"
# ]])

# Dates ko sort karna
result = employees.sort_values(
    "Joining_Date",
    ascending=False
)

# print(result[["Name", "Joining_Date"]])

# Date ke basis par filtering
result2 = employees[
    employees["Joining_Date"] > "2023-01-01"
]

# print(result2)

# sirf 2023 mein join karne wale employees.
result3 = employees[
    employees["Joining_Date"].dt.year == 2023
]

# print(result3)

# Date difference calculate karna
today = pd.Timestamp("2026-11-04")

employees["Days_Worked"] = (
    today - employees["Joining_Date"]
).dt.days

# print(employees[["Name", "Joining_Date", "Days_Worked"]])

dates2 = pd.Series([
    "2026-01-15",
    "2026-02-20",
    "invalid-date",
    None,
    "2026-04-10"
])

date3 = pd.to_datetime(
    dates2,
    errors="coerce"
)
# print(date3)
# print(date3.isnull())

clean_dates = dates2.dropna()
# print(clean_dates)


# Mini - Project
employees2 = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Joining_Date": [
        "2023-01-15",
        "2022-06-20",
        "2024-03-10",
        "2021-12-05",
        "2023-08-25"
    ],
    "Salary": [35000, 42000, 38000, 50000, 32000]
})

# convert joining date into datetime
employees2["Joining_Date"] = pd.to_datetime(
    employees2["Joining_Date"]
)

# Extract Year
employees2["Joining_Year"] = (
    employees2["Joining_Date"].dt.year
)

# Extract month name
employees2["Joining_Month"] = (
    employees2["Joining_Date"].dt.month_name()
)

# Extract day name
employees2["Joining_Day"] = (
    employees2["Joining_Date"].dt.day_name()
)

# Calculate days worked
today = pd.Timestamp("2026-11-04")

employees2["Days_Worked"] = (
    today - employees2["Joining_Date"]
).dt.days

# Display latest joining employees
latest_employees = employees2.sort_values(
    "Joining_Date",
    ascending=False
)

print("Employee Joining Date Analysis:")
print(latest_employees)