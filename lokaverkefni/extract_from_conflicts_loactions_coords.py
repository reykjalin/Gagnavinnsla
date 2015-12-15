# coding=utf-8
import numpy as np
import pandas as pd
import datetime

locations_cooords_column_names = ('location','lat','long')


conflict_location_cords = pd.read_csv('locations_coords.csv', sep=",", engine='python'\
	,encoding='UTF-8',names=locations_cooords_column_names,index_col=0)

schema_conflict_location_cords = ("""create table conflictlc (
location varchar(250),
lat varchar(250),
long varchar(250),
primary key (location));
""")

outs = open('schema_conflict_location_cords.txt', 'w')
outs.write(schema_conflict_location_cords)
outs.close()

