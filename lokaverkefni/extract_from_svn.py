import numpy as np
import pandas as pd
import datetime




eclipse_column_names = ('catalognumber','calendardate_year','calendardate_month','calendardate_day',\
<<<<<<< .mine
	'greatesteclipse_td','dT','luna_num','saros_num','ecl_type',\
||||||| .r219
	'greatesteclipse_dt','luna_num','saros_num','ecl_type',\
=======
	'greatesteclipse_dt','dT','luna_num','saros_num','ecl_type',\
>>>>>>> .r222
	'qle','gamma','ecl_mag',\
	'lat','long','sun_alt',\
	'path_width','central_dur')


eclipse1900_2001 = pd.read_csv('eclipse_1901_2000.csv', sep="[  ]+", engine='python'\
	,encoding='UTF-8',names=eclipse_column_names,index_col=0)
# eclipse1900_2001.index.name = 'index'
for i in range(len(eclipse1900_2001)):
	if (eclipse1900_2001['calendardate_month'][i]) = ('May') # HOW TOOOO !
		print('Yay!')
	else:
		print('naa')

eclipse1900_2001["calendardate"] = eclipse1900_2001["calendardate_year"].map(str) + eclipse1900_2001["calendardate_month"].map(str) + eclipse1900_2001["calendardate_day"].map(str) 

<<<<<<< .mine
eclipse1900_2001['calendardate_month'] = '-' + eclipse1900_2001['calendardate_month'].astype(str)
eclipse1900_2001['calendardate_day'] = '-' + eclipse1900_2001['calendardate_day'].astype(str)

eclipse1900_2001["calendardate"] = eclipse1900_2001["calendardate_year"].map(str) +  \
eclipse1900_2001["calendardate_month"].map(str) + eclipse1900_2001["calendardate_day"].map(str)

# print(datetime.strptime("19", "%d/%m/%Y").strftime('%Y-%m-%d'))


||||||| .r219
=======

eclipse1900_2001 = eclipse1900_2001.drop('calendardate_year',1)
eclipse1900_2001 = eclipse1900_2001.drop('calendardate_month',1)
eclipse1900_2001 = eclipse1900_2001.drop('calendardate_day',1)

eclipse1900_2001 = eclipse1900_2001[['catalognumber','calendardate',\
	'greatesteclipse_dt','dT','luna_num','saros_num','ecl_type',\
	'qle','gamma','ecl_mag',\
	'lat','long','sun_alt',\
	'path_width','central_d']]

#print(eclipse1900_2001)
>>>>>>> .r222
eclipse1900_2001.to_csv('output.csv',sep=';', encoding='utf-8')
#print(eclipse1900_2001.head())

# 'calendardate_year','calendardate_month','calendardate_day'