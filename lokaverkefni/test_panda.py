import numpy as np
import pandas as pd
import datetime

export = pd.read_csv('TIV-Export-All-1950-2014.csv', sep=",", engine='python'\
	,encoding='UTF-8', skiprows=range(0, 10))
# export.set_index('type', inplace = True)
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

export.to_csv('output_export.csv',sep=';', encoding='utf-8')

print(export.head())
print(years)



# export2 = export.stack()


# print(types)
# create table movies (
# id varchar(250),
# title varchar(250),
# year varchar(250),
# rating float,
# primary key (id)
# );