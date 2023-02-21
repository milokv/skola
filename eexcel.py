import pandas as pd
dataframe1 = pd.read_excel('pyexcel.xlsx')
print(dataframe1)
dataframe1.to_excel('panda.xlsx')
