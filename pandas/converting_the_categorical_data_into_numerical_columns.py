import pandas as pd
path=r"dataset.csv"
file=pd.read_csv(path)
df=pd.DataFrame(file)
print(df.shape)

