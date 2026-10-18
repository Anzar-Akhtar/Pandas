import pandas as pd

employees = pd.DataFrame({
    "Name": [" alex ", "HONEY", "curran", "John Smith", "Chris"],
    "Department": ["IT", "finance", "IT", "Networking", "Finance"],
    "Email": [
        "alex@gmail.com",
        "HONEY@GMAIL.COM",
        "curran@yahoo.com",
        "john@gmail.com",
        "chris@yahoo.com"
    ]
})

# print(employees)
print()

# str.lower() — Text ko lowercase karna
employees["Name_Lower"] = employees["Name"].str.lower()
# print(employees[["Name", "Name_Lower"]])


# str.upper() — Text ko uppercase karna
employees["Name_Upper"] = employees["Name"].str.upper()
# print(employees[["Name", "Name_Upper"]])


# str.title() — Har word ka first letter capital
employees["Name_Title"] = employees["Name"].str.title()
# print(employees[["Name", "Name_Title"]])


# str.strip() — Extra spaces remove karna
employees["Name_Clean"] = employees["Name"].str.strip()
# print(employees[["Name", "Name_Clean"]])


# str.replace() — Text replace karna
employees["Email_Updated"] = (
    employees["Email"].str.lower().str.replace(
        "gmail.com", "example.com", regex=False
    )
)
# print(employees[["Email", "Email_Updated"]])


# str.contains() — Text search karna
gmail_employees = employees[
    employees["Email"].str.contains("gmail", case=False, na=False)
]
# print(gmail_employees)


# str.startswith() — Starting text check karna
result1 = employees[
    employees["Email"].str.startswith("alex", na=False)
]
print(result1)


# str.endswith() — Ending text check karna
result2 = employees[
    employees["Email"].str.endswith("yahoo.com", na=False)
]
print(result2)


# str.len() — Text ki length calculate karna
employees["Name_Length"] = (
    employees["Name"].str.strip().str.len()
)
print(employees[["Name", "Name_Length"]])


# str.split() — Full name ko split karna
employees["Full_Name"] = [
    "Alex Khan",
    "Honey Sharma",
    "Curran Singh",
    "John Smith",
    "Chris Verma"
]

employees[["First_Name", "Last_Name"]] = (
    employees["Full_Name"].str.split(" ", n=1, expand=True)
)
print(employees[["Full_Name", "First_Name", "Last_Name"]])