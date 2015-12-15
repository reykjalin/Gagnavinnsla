# coding=utf-8
import numpy as np
import pandas as pd
import datetime

eclipse_column_names = ('catalognumber','calendardate_year','calendardate_month','calendardate_day',\
	'greatesteclipse_td','dt','luna_num','saros_num','ecl_type',\
	'qle','gamma','ecl_mag',\
	'lat','long','sun_alt',\
	'path_width','central_dur')


eclipse = pd.read_csv('DB/eclipse.csv', sep="[  ]+", engine='python'\
	,encoding='UTF-8',names=eclipse_column_names,index_col=0)
# eclipse.index.name = 'index'


eclipse['calendardate_month'] = '-' + eclipse['calendardate_month'].astype(str)
eclipse['calendardate_day'] = '-' + eclipse['calendardate_day'].astype(str)

eclipse["calendardate"] = eclipse["calendardate_year"].map(str) +  \
eclipse["calendardate_month"].map(str) + eclipse["calendardate_day"].map(str) + ' ' +  eclipse['greatesteclipse_td'].map(str)

eclipse["calendardate"] = pd.to_datetime(eclipse["calendardate"])

# create schema
eclipse = eclipse.drop(eclipse.columns[[1, 2]], axis = 1)
# eclipse = eclipse.convert_objects(convert_numeric=True)


schema_eclipse = ("""create table eclipse (
catalognumber real,
calendardate_year real,
greatesteclipse_td time,
dt real,
luna_num real,
saros_num real,
ecl_type varchar(250),
qle varchar(250),
gamma real,
ecl_mag real,
lat varchar(250),
long varchar(250),
sun_alt real,
path_width real,
central_dur varchar(250),
calendardate date,
primary key (calendardate_year));
""")

outs = open('DB/schema_eclipse.txt', 'w')
outs.write(schema_eclipse)
outs.close()


# eclipse = eclipse.drop(eclipse.columns[[0, 1, 2]], axis = 1)


# geolocator = Nominatim()

# lat = eclipse['lat'].tolist()
# lon = eclipse['long'].tolist()
# land = []

# for i in range(len(eclipse)):

# 	if lat[i].endswith('N'): ## Norður + , Suður -
# 		lat[i] = int(lat[i][:-1])
# 	else:		
# 		lat[i] = int('-' + lat[i][:-1])

# 	if lon[i].endswith('E'): # Astur +. Vestur -
# 		lon[i] = int(lon[i][:-1])
# 	else:		
# 		lon[i] = int('-' + lon[i][:-1])




# eclipse['lat'] = lat
# eclipse['long'] = lon
