import numpy as np
import pandas as pd

eclipse_column_names = ('catalognumber','calendardate','greatesteclipse_dt',\
	'luna_num','saros_num','ecl_type',\
	'qle','gamma','ecl_mag',\
	'lat','long','sun_alt',\
	'path_width','central_d')
eclipse1900_2001 = pd.read_csv('eclipse_1901_2000.csv', encoding='UTF-8',names=eclipse_column_names)
print(eclipse1900_2001.head())