import pandas as pd

df = pd.read_csv("day3/students.csv")
print(df)

print(df["Name"])
print(df["Age"])
print(df[["Name", "Age", "Marks"]])


# iloc means:- position number ke basis pr data select karna
print(df.iloc[0])
print(df.iloc[1])


print(df.iloc[0:3])

# specific cell with iloc
print(df.iloc[0, 3])

# iloc se rows + column
print(df.iloc[0:3, 0:2])

# loc:-ka use labels ke basis par selection ke liye hota hai.
print(df.loc[0, "Name"])
print(df.loc[0, "Marks"])

print(df.loc[0:4, ["Name", "Marks"]])