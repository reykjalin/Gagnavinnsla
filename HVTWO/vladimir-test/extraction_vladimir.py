import numpy as np
import pandas as pd


MovieDatabse = pd.read_csv('movies.csv',sep = ',', encoding='UTF-8',index_col=0)
MovieDatabse['year']= MovieDatabse ['title'].str.extract('(\d\d\d\d)')
MovieDatabse['title'] = [i.rsplit('(',1)[0].strip() for i in MovieDatabse['title']]
# theyear = [int(i.rsplit('(',1)[1].rstrip(')')) for i in MovieDatabse.title]
print(MovieDatabse.head)
