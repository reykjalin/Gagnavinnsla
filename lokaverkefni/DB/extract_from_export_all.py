# coding=utf-8
import numpy as np
import pandas as pd
import datetime

export = pd.read_csv('DB/TIV-Export-All-1950-2014.csv', sep=",", engine='python'\
	,encoding='UTF-8', skiprows=range(0, 10))
export.set_index('type', inplace = True)
export = export.drop('deleteme', 1)
export.fillna('0', inplace=True)

#rearenge the table
types = []
years = []
price = []
for col in export.columns:
        for i in export.index:
                types.append(i)
                years.append(col)
                price.append(export[col][i])
               
export_sql = pd.DataFrame()
export_sql['type'] = types
export_sql['year'] = years
export_sql['price'] = price
export_sql.index.name = 'index_export'
# remove total price
export_sql = export_sql[export_sql.year != 'total']
export_sql = export_sql.apply(pd.to_numeric, errors='coerce')

# create schema

schema_export = ("""create table export (
type varchar(250),
year date,
price real,
index_export real,
primary key (index_export));
""")

outs = open('DB/schema_export.txt', 'w')
outs.write(schema_export)
outs.close()

