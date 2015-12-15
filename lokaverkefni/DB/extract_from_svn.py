# coding=utf-8
import numpy as np
import pandas as pd
import datetime
from geopy.geocoders import Nominatim 
import pprint as pp
import WorldDomination
import libs.SpinTest

eclipse_column_names = ('catalognumber','calendardate_year','calendardate_month','calendardate_day',\
	'greatesteclipse_td','dT','luna_num','saros_num','ecl_type',\
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

# print(datetime.strptime("19", "%d/%m/%Y").strftime('%Y-%m-%d'))

eclipse["calendardate"] = pd.to_datetime(eclipse["calendardate"])

eclipse = eclipse.drop(eclipse.columns[[0, 1, 2]], axis = 1)


geolocator = Nominatim()

lat = eclipse['lat'].tolist()
lon = eclipse['long'].tolist()
land = []

for i in range(len(eclipse)):

	if lat[i].endswith('N'): ## Norður + , Suður -
		lat[i] = int(lat[i][:-1])
	else:		
		lat[i] = int('-' + lat[i][:-1])

	if lon[i].endswith('E'): # Astur +. Vestur -
		lon[i] = int(lon[i][:-1])
	else:		
		lon[i] = int('-' + lon[i][:-1])




eclipse['lat'] = lat
eclipse['long'] = lon
#print(eclipse.head())

###########
# for i in range(len(lat)):
# 	try:
# 		location = geolocator.reverse("{},{}".format(lat[i],lon[i]))
# 	except:
# 		pass	

# 	try:
#  		land[i] = location.address.rsplit(", ",1)[1]
#  		print(land[i])
# 	except:
# 		land.append('X')

##########	

# print(type(land))

# eclipse['country'] = land

# print(eclipse)

a = 60
b = 75

count = 0
for g in lat:
	if ((g > a) and (g < b)) or ((g < -a) and (g > -b)):
		count +=1

# The number of solar eclipses between (lat 60 and 75) and (lat -60 and -75)
print(count/(len(lat)))

x = list(eclipse["calendardate"])

#WorldDomination.plotme(lat,lon,land,x)
#SpinTest.plotme(lat,lon)
SpinTest.plot2D(lat,lon,land)


#eclipse.to_csv('output_eclipse.csv',sep=';', encoding='utf-8')

#print(eclipse.head())

# 'calendardate_year','calendardate_month','calendardate_day'
