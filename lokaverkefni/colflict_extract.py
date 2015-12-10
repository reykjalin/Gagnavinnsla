import numpy as np
import pandas as pd


conflict = pd.read_csv('armed-conflict-dataset.csv', sep=",", engine='python'\
	,encoding='UTF-8')
conflict.index.name = 'index_conflict'

outs = open('scehma.txt', 'a',encoding = "UTF-8")
outs.write(\
"""create table conflict (
index_conflict 
conflictid
year
location
sidea
sidea2nd
sideb
sidebid
sideb2nd
incompatibility
territoryname
intensitylevel
cumulativeintensity
typeofconflict
startdate
startprec
startdate2
startprec2
epend
ependdate
ependprec
gwnoa
gwnoa2nd
gwnob
gwnob2nd
gwnoloc
region
version
primary key (index_conflict)
);
""")

outs.close()

print(conflict.head())

