import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95]
})

print(students)
print("Shape: ", students.shape)
print("\nDimension: ", students.ndim)
print("\nSize: ", students.size)
print("\nColumns: ", students.columns)
print("\nIndex: ", students.index)
print("\nData Type:")
print(students.dtypes)
print("\nDataFrame Information:")
print(students.info())
print("\nStatistical Summary:")
print(students.describe())
print("\nFirst 3 Rows:")
print(students.head(3))
print("\nLast 2 Rows:")
print(students.tail(2))
print("\nRandom 2 Rows:")
print(students.sample(2))
print("\nNumber of Rows: ", len(students))