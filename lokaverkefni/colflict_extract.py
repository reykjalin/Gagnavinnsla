import numpy as np
import pandas as pd


conflict = pd.read_csv('armed-conflict-dataset.csv', sep=",", engine='python'\
	,encoding='UTF-8',index_col=0)

conflict.colums = map(str.lower, conflict.columns)




print(conflict.head())

