# dataframe:- ek 2D labeled data structure hai like excel spreadsheet or database

import pandas as pd

data = {
    "Name": ["alex", "honey", "curran"],
    "Age": [20, 21, 22],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)
print(df)