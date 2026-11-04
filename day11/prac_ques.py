import pandas as pd

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