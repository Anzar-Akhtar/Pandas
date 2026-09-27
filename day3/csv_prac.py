import pandas as pd

df = pd.read_csv("day3/students.csv")
print(df)

print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())