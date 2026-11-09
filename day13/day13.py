import pandas as pd

data = pd.DataFrame({
    "Name": ["Alex", "John", "Alex", "Honey", "Chris"],
    "Age": [20, 21, 20, 22, 20],
    "Marks": [85, 90, 85,  None, 75]
})

print(data)

print(data.duplicated())

print(data.duplicated().sum())

# drop_duplicates() – Duplicate records remove karna
clean_data = data.drop_duplicates()
print(clean_data)

# Specific column ke basis par duplicate check
print(data.duplicated(subset=["Name"]))


data = pd.DataFrame({
    "Name": ["Alex", "John", "Honey"],
    "Age": ["20", "21", "22"],
    "Marks": ["85", "90", "88"]
})

print(data.dtypes)

data["Age"] = data["Age"].astype(int)
data["Marks"] = data["Marks"].astype(int)

print(data.dtypes)



# replace() – Incorrect values replace karna
data2 = pd.DataFrame({
    "Name": ["Alex", "John", "Honey", "Chris"],
    "Department": ["AI", "ai", "Artificial Intelligence", "Cloud"]
})

print(data2)

data2["Department"] = data2["Department"].replace({
    "ai" : "AI",
    "Artificial Intelligence": "AI"
})
print(data2)

# multiple values together
data2["Department"] = data2["Department"].replace(
    ["AI", "Cloud"],
    ["Artificial Intelligence", "Cloud Computing"]
)
print(data2)

data3 = pd.DataFrame({
    "Name": [" alex ", "JOHN", "Honey ", " chris"],
    "City": ["delhi", "DELHI", "Agra", "agra"],
    "Gender": ["M", "Male", "F", "Female"]
})

print(data3)

# remove extra spaces and standardize names
data3["Name"] = data["Name"].str.strip().str.title()

# standardize city names
data3["City"] = data3["City"].str.strip().str.title()

# standardize gender values
data3["Gender"] = data3["Gender"].replace({
    "M": "Male",
    "F": "Female"
})

print(data3)