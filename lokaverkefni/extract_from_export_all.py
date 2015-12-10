import numpy as np
import pandas as pd
import datetime

export = pd.read_csv('TIV-Export-All-1950-2014.csv', sep=",", engine='python'\
	,encoding='UTF-8', skiprows=range(0, 10))
export.set_index('type', inplace = True)
export = export.drop('deleteme', 1)
export.fillna('0', inplace=True)



outs = open('scehma.txt', 'w',encoding = "UTF-8")
outs.write("""create table Export (""")

# types = export['type'].values.tolist()
years = str([x for x in range(1950,2014)]).strip('[]')

for i in range (1950,2014):    
	outs.write("""{} date,\n""".format(i))

outs.write("""{} character(250),
			primary key ({}) """.format('type','type'))

outs.close()


print(export.head())
print(export.columns)


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
print(sqltable)
# export2 = export.stack()


# print(types)
# create table movies (
# id varchar(250),
# title varchar(250),
# year varchar(250),
# rating float,
# primary key (id)
# );
