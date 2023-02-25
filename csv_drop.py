import pandas as pd
data=pd.read_csv("size.csv")
data=pd.DataFrame(data)
data=data.dropna()
d=data.to_csv("size.csv")