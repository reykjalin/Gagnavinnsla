import numpy as np
import pandas as pd
import datetime

export = pd.read_csv('TIV-Export-All-1950-2014.csv', sep="[  ]+", engine='python'\
	,encoding='UTF-8',names=eclipse_column_names,index_col=0)
print(export.head())