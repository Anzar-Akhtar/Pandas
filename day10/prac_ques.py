import pandas as pd
import numpy as np

employees = pd.DataFrame1({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        " alex ", "HONEY", "curran ", "JOHN SMITH", " chris",
        "RAHUL SHARMA ", "priya", " AMAN ", "NEHA GUPTA", "rohit"
    ],
    "Department": [
        "IT", "finance", " IT ", "HR", "Finance",
        "hr ", "IT", "FINANCE", " HR", "it"
    ],
    "Email": [
        "alex@gmail.com", "HONEY@GMAIL.COM", "curran@yahoo.com",
        "john@gmail.com", "chris@outlook.com", "rahul@yahoo.com",
        "priya@gmail.com", "aman@outlook.com", "neha@yahoo.com",
        "rohit@gmail.com"
    ],
    "City": [
        "delhi", "MUMBAI", "delhi ", "PUNE", "mumbai",
        " DELHI", "pune", "MUMBAI ", "delhi", "PUNE"
    ],
    "Salary": [35000, 42000, 38000, 50000, 32000, 45000, 40000, 36000, 48000, 39000]
})

# print(employees)

# Question1:- convert name into lowercase()
employees["lower_name"] = employees["Name"].str.lower()
# print(employees["lower_name"])

# Question2:- clean and format names.
employees["clean_name"] = employees["Name"].str.strip()
print(employees["clean_name"])

# Question3:- filter gmail users.
employees["clean_email"] = employees["Email"].str.strip()
print(employees["clean_email"])

