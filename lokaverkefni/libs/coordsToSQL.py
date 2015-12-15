# coding=utf-8
from get_coords import get_coords, get_loc
import psycopg2
import pprint as pp
import pandas as pd
import csv

host = 'localhost'
# db = input('Enter the Database name: ')
# usr = input('Username: ')
# pw = input('Password: ')
db = 'finalproj'
usr = 'kristofer'
pw = 'Krissicool2'

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, db, usr, pw)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


dictionary = {}
s = """select distinct lat, long from eclipse;"""

cursor.execute(s)
coords = cursor.fetchall()
cursor.close()
conn.close()

templocations = []

######################### For coordinates to locations #########################
lats = []
lons = []
for i in range(len(coords)):
    if coords[i][0].endswith('N'): # N: +, S: -
        lats.append(int(coords[i][0][:-1]))
    else:
        lats.append(int('-' + coords[i][0][:-1]))
        
    if coords[i][1].endswith('E'): # E: +, W: -
        lons.append(int(coords[i][1][:-1]))
    else:
        lons.append(int('-' + coords[i][1][:-1]))

locs = get_loc(lats, lons)
with open('locations_eclipse.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(len(lats)):
        writer.writerow([lats[i], lons[i], locs[i]])

######################### For locations to coordinates #########################
# for i in range(len(locations)):
# 	locations[i] = locations[i][0].split(',')
# 	for j in range(len(locations[i])):
# 		templocations.append(locations[i][j].strip())

# locations = list(set(templocations))

#pp.pprint(locations)

#lat, lon = get_coords(locations)

#location = [locations,lat,lon]

# location = pd.DataFrame(location)

# with open('locations_coords.csv', 'w') as f:
#     writer = csv.writer(f)
#     for i in range(len(locations)):
#     	writer.writerow([locations[i], lat[i], lon[i]])


# location_df = pd.DataFrame()
# location_df.index.name = 'index_location'
# location_df['location'] = location
# location_df['lat'] = lat
# location_df['lon'] = lon

# # remove total price
# location_df = location_df.apply(pd.to_numeric, errors='coerce')



#Skrifa location í database 
# pp.pprint(location_df)
