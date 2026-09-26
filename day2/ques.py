import pandas as pd

students = pd.DataFrame({
    "Name": ["Alex", "Honey", "Curran", "John", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88, 95]
})

# Question1:- find the shape, ndim, size, column, index
# print("shape=", students.shape)
# print("\nDimension=", students.ndim)
# print("\nSize=", students.size)
# print("\ncolumns=", students.columns)
# print("\nIndex=", students.index)

# Question2:- create employee dataframe and check the datatype of each column

employee = {
    "Name": ["person1", "person2", "person3", "person4"],
    "Age": [20, 23, 24, 21],
    "Salary": [24000, 25000, 30000, 32000],
    "Experience": [1, 2, 3, 4]
}

df = pd.DataFrame(employee)
# print(df)

# print(df.dtypes)

# Question3:- Find the info of the students dataframe
# print(students.info())

# Question4:- make the series and describe it
series = pd.Series([65, 72, 80, 91, 88, 76, 95])
# print(series.describe())

# Question5:- AI/ML Dataset
data = {
    "Age": [20, 25, 30, 35, 40],
    "Experience": [1, 3, 5, 7, 10],
    "Salary": [25000, 40000, 60000, 80000, 100000]
}
df2 = pd.DataFrame(data)
print(df2)
print("\nShape=", df.shape)
print("\nNo. of Rows=", len(df2))
print("\nNo. of Column=", df2.columns)
print("\nData Type=", df2.dtypes)
print("\nStatistical Summary=", df2.describe())
print("\nFirst 3 Rows=", df2.head(3))
print("\nLast 2 Rows=", df2.tail(2))