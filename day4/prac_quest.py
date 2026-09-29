import pandas as pd
df = pd.read_csv("day3/students.csv")

print(df)

# Question1:- print the name marks attendence in single column.
print(df["Name"])
print(df["Marks"])
print(df["Attendance"])

# Question2:- Multiple Columns
print(df[["Name", "Marks"]])
print(df[["Name", "Age", "Attendance"]])

# Question3:- iloc
print(df.iloc[0])
print(df.iloc[2])
print(df.iloc[0:5])
print(df.iloc[-5:])

# Question4:- Specific Value
print(df.iloc[0, 3])
print(df.iloc[1, 1])
print(df.iloc[4, 4])