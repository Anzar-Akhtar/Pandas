# series ek 1D labeled data structure hai

import pandas as pd

data = pd.Series([10,20,30,40])
# print(data)

# custom indexing
marks = pd.Series(
    [80, 90, 75],
    index = ["alex", "honey", "curran"]
)
print(marks)