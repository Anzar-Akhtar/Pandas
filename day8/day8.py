import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95],
    "Attendance": [92, 95, 88, 90, 97]
})

df = students
print(df)
print()

# sort_values() ka use kisi column ke according rows ko arrange karne ke liye hota hai.
# ascending order
# print(df.sort_values("Marks"))

# descending order
# print(df.sort_values("Marks", ascending=False))

# multiple column sorting
# print(
#     df.sort_values(
#         ["Age", "Marks"]
#     )
# )

# Different order for different columns
# print(
#     df.sort_values(
#         ["Age", "Marks"],
#         ascending=[True, False]
#     )
# )

# Agar original data frame ko change karna hai to use (inplace=True)

# sort_index() row index ke according sorting karta hai.
# print(df.sort_index(ascending=False))

# rank():- is used to give the ranking to the students
df["Rank"] = df["Rank"] = df["Marks"].rank(ascending=False).astype(int)
# print(df[["Name", "Marks", "Rank"]])

df2 = pd.DataFrame({
    "Name": ["Alex", "Honey", "John", "Chris"],
    "Marks": [90, 80, 90, 70]
})

# same marks hone par ranking
df2["Rank"] = df["Marks"].rank(ascending=False)
# print(df2)

# Ranking Methods
# (avg)
df2["Rank"] = df2["Marks"].rank(ascending=False, method="average")
# print(df2)

# (min)
df2["Rank"] = df2["Marks"].rank(ascending=False, method="min")
print(df2)
