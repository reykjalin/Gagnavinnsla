import numpy as np
import pandas as pd
import datetime
from geopy.geocoders import Nominatim 
import pprint as pp




eclipse_column_names = ('catalognumber','calendardate_year','calendardate_month','calendardate_day',\
	'greatesteclipse_td','dT','luna_num','saros_num','ecl_type',\
	'qle','gamma','ecl_mag',\
	'lat','long','sun_alt',\
	'path_width','central_dur')


eclipse = pd.read_csv('eclipse.csv', sep="[  ]+", engine='python'\
	,encoding='UTF-8',names=eclipse_column_names,index_col=0)
# eclipse.index.name = 'index'


eclipse['calendardate_month'] = '-' + eclipse['calendardate_month'].astype(str)
eclipse['calendardate_day'] = '-' + eclipse['calendardate_day'].astype(str)

eclipse["calendardate"] = eclipse["calendardate_year"].map(str) +  \
eclipse["calendardate_month"].map(str) + eclipse["calendardate_day"].map(str)

# print(datetime.strptime("19", "%d/%m/%Y").strftime('%Y-%m-%d'))

eclipse["calendardate"] = pd.to_datetime(eclipse["calendardate"])

eclipse = eclipse.drop(eclipse.columns[[0, 1, 2]], axis=1)


geolocator = Nominatim()


lat = eclipse['lat'].tolist()
lon = eclipse['long'].tolist()
land = list()

for i in range(len(eclipse)):

	if lat[i].endswith('N'):
		lat[i] =lat[i][:-1]
	else:		
		lat[i] = '-' + lat[i][:-1]

	if lon[i].endswith('E'):
		lon[i] =lon[i][:-1]
	else:		
		lon[i] = '-' + lon[i][:-1]

print(type(lat))
eclipse['land'] = lat
print(eclipse.head())




for i in range(len(lat)):
	try:
		location = geolocator.reverse("{},{}".format(lat[i],lon[i]))
	except:
		land[i] = lat[i]
	try:
 		land[i] = location.address.rsplit(", ",1)[1]
 		print(land[i])
	except:
		pass
	

print(type(land))

eclipse['country'] = land

print(eclipse)






#eclipse.to_csv('output_eclipse.csv',sep=';', encoding='utf-8')

#print(eclipse.head())

# 'calendardate_year','calendardate_month','calendardate_day'