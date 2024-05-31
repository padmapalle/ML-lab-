# -*- coding: utf-8 -*-
#JYOTHIKA C N
#1BM21CS083
import pandas as pd
df=pd.read_csv("austinHousingData.csv")
print(df.head())
df.to_csv("exported_dataset.csv")