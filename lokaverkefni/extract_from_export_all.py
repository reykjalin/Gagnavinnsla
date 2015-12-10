import numpy as np
import pandas as pd
import datetime

export = pd.read_csv('TIV-Export-All-1950-2014.csv', sep=",", engine='python'\
	,encoding='UTF-8', skiprows=range(0, 10))
export.set_index('type', inplace = True)
export = export.drop('deleteme', 1)
export.fillna('0', inplace=True)

#rearenge the table
types = []
years = []
data = []
for col in export.columns:
        for i in export.index:
                types.append(i)
                years.append(col)
                data.append(export[col][i])
               
sqltable = pd.DataFrame()
sqltable['type'] = types
sqltable['year'] = years
sqltable['data'] = data
sqltable.index.name = 'index_export'
# remove total price
sqltable = sqltable[sqltable.year != 'total']


# create schema
outs = open('scehma_export.txt', 'w',encoding = "UTF-8")
outs.write(\
"""create table Export (
type varchar(250),
year date,
data real,
index_export real,
primary key (index_export));
""")

outs.close()



# create table movies (
# id varchar(250),
# title varchar(250),
# year varchar(250),
# rating float,
# primary key (id)
# );
