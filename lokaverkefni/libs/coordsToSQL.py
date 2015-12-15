# coding=utf-8
from get_coords import get_coords
import psycopg2
import pprint as pp
import pandas as pd

host = 'localhost'
# db = input('Enter the Database name: ')
# usr = input('Username: ')
# pw = input('Password: ')
db = 'asdasd'
usr = 'postgres'
pw = 'postgres'

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, db, usr, pw)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


dictionary = {}
s = """select distinct location from conflict
order by location ;"""

cursor.execute(s)
locations = cursor.fetchall()
cursor.close()
conn.close()

templocations = []


for i in range(len(locations)):
	locations[i] = locations[i][0].split(',')
	for j in range(len(locations[i])):
		templocations.append(locations[i][j].strip())

locations = list(set(templocations))

#pp.pprint(locations)

[lat,lon] = get_coords(locations)

location = [locations,lat,lon]

# location = pd.DataFrame(location)

with open('locations_coords.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in itertools.izip(locations,lat,lon):
    	writer.writerow(val)


# location_df = pd.DataFrame()
# location_df.index.name = 'index_location'
# location_df['location'] = location
# location_df['lat'] = lat
# location_df['lon'] = lon

# # remove total price
# location_df = location_df.apply(pd.to_numeric, errors='coerce')



#Skrifa location í database 
# pp.pprint(location_df)