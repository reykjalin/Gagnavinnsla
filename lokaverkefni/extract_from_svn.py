import numpy as np
import pandas as pd
import datetime as dt



eclipse_column_names = ('catalognumber','calendardate_year','calendardate_month','calendardate_day',\
	'greatesteclipse_dt','luna_num','saros_num','ecl_type',\
	'qle','gamma','ecl_mag',\
	'lat','long','sun_alt',\
	'path_width','central_d')

parser = lambda date: pd.datetime.strptime(date, '%d %b %Y')

eclipse1900_2001 = pd.read_csv('eclipse_1901_2000.csv', sep="[  ]+", engine='python'\
	,encoding='UTF-8',names=eclipse_column_names)
eclipse1900_2001.index.name = 'index'


eclipse1900_2001.to_csv('output.csv',sep=';', encoding='utf-8')
print(eclipse1900_2001.head())

# 'calendardate_year','calendardate_month','calendardate_day'