import numpy as np
import pandas as pd


conflict = pd.read_csv('armed-conflict-dataset.csv', sep=",", engine='python'\
	,encoding='UTF-8')
conflict.index.name = 'index_conflict'
conflict = conflict.convert_objects(convert_numeric=True)


schema_conflict = ("""create table conflict (
index_conflict real,
conflictid varchar(250),
year date,
location varchar(250),
sidea varchar(250),
sidea2nd varchar(250),
sideb varchar(250),
sidebid real,
sideb2nd real,
incompatibility real,
territoryname varchar(250),
intensitylevel real,
cumulativeintensity real,
typeofconflict real,
startdate date,
startprec real,
startdate2 date,
startprec2 real,
epend real,
ependdate date,
ependprec real,
gwnoa real,
gwnoa2nd real,
gwnob real,
gwnob2nd real,
gwnoloc real,
region real,
version varchar(250),
primary key (index_conflict));
""")

outs = open('scehma_conflict.txt', 'w',encoding = "UTF-8")
outs.write(schema_conflict)
outs.close()

