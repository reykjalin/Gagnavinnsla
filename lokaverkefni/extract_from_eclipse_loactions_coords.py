# coding=utf-8
import numpy as np
import pandas as pd
import datetime

locations_cooords_column_names = ('lat','long','location')


eclipse_location_cords = pd.read_csv('locations_eclipse.csv', sep=",", engine='python'\
	,encoding='UTF-8',names=locations_cooords_column_names,index_col=0)

schema_eclipse_location_cords = ("""create table eclipselc (
lat varchar(250),
long varchar(250),
location varchar(250),
primary key (lat)
primary key (long));
""")

outs = open('schema_eclipse_location_cords.txt', 'w')
outs.write(schema_eclipse_location_cords)
outs.close()
