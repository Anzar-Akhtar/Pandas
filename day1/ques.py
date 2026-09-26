import pandas as pd

# Queston 1:- Create a Series
data = pd.Series([10,20,30,40,50])
print(data)

# Question 2:- Custom Indexing
data2 = pd.Series(
    [85,92,76,88],
    index=["alex","honey","curran","john"]
)
print(data2)

# Question 3:- Basic DataFrame
data3 = {
    "Name": ["alex", "honey", "curran", "john"],
    "Age": [20, 21, 20, 22],
    "Course": ["BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 92, 76, 88]
}
df = pd.DataFrame(data3)
print(df)

# Question 4:- Employee DataFrame
data4 = {
    "Name": ["alex", "honey", "curran", "john", "Chris"],
    "Age": [20, 21, 20, 22, 23],
    "Department": ["IT", "Finace", "Networking", "IT", "finance"],
    "Salary": [25000, 27000, 20000, 30000, 23000],
    "Experience": [1, 2, 1, 3, 2]
}
df2 = pd.DataFrame(data4)
print(df2)

# Question 5:- AI/ML Dataset
data5 = {
    "Age": [20, 21, 20, 22, 23],
    "Experience": [1, 2, 1, 3, 2],
    "Salary": [25000, 27000, 20000, 30000, 23000]
}
df3 = pd.DataFrame(data5)
print(df3)
