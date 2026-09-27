import pandas as pd

df_csv = pd.read_csv("day3/students.csv")
df_excel = pd.read_excel("day3/students_20.xlsx")
df_json = pd.read_json("day3/students_20.json")

# Question1:- print completer dataframe, first 5 rows, last 5 rows

frame1 = pd.DataFrame(df_csv)
print("COMPLETE DATAFRAME:")
print(frame1)

print("FIRST 5 ROWS:")
print(frame1.head(5))

print("LAST 5 ROWS:")
print(frame1.tail(5))