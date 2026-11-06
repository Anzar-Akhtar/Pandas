import pandas as pd

data = pd.DataFrame({
    "Name": [" alex ", "JOHN", "Alex", "Honey ", "Chris"],
    "Age": ["20", "21", "20", "22", "Invalid"],
    "Marks": [85, 90, 85, None, 75],
    "Department": ["AI", "ai", "AI", "Cloud", "cloud"]
})

print("Original Dataset:")
print(data)

# 1:- Clean Names
data["Name"] = data["Name"].str.strip().str.title()

# 2:- Convert Age into Numeric
data["Age"] = pd.to_numeric(
    data["Age"],
    errors="coerce"
)

# 3:- Standardize department
data["Department"] = (
    data["Department"].str.strip().str.upper()
)

# 4:- Remove duuplicate rows
data = data.drop_duplicates()

# 5:- fill missing marks with mean
data["Marks"] = data["Marks"].fillna(
    data["Marks"].mean()
)

# 6:- remove rows with missing age
data = data.dropna(subset=["Age"])

print("\nCleaned Dataset:")
print(data)

print("\nData Types:")
print(data.dtypes)