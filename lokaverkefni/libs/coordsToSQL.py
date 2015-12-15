from get_coords import get_coords
import psycopg2
import pprint as pp

host = 'localhost'
db = input('Enter the Database name: ')
usr = input('Username: ')
pw = input('Password: ')

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

loclatlon = [locations,lat,lon]

#Skrifa loclatlon í database 
pp.pprint(loclatlon)