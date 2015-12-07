import psycopg2 as sql
import getpass

host = 'localhost'
dbname = 'movielens_sm'
username = 'kristofer'
pw = getpass.getpass()

conn_string = "host = '{}' dbname = '{}' user = '{}' password = '{}'".format(host, dbname, username, pw)

print('Connecting to database: {}.{} as {}'.format(host, dbname, username))
conn = sql.connect(conn_string)
cursor = conn.cursor()

print("Connected!\n")

sqlcmds = open('insert_to_movielens.sql', 'r')
for line in sqlcmds:
    cursor.execute(line.strip())

sqlcmds.close()
conn.commit()
cursor.close()
conn.close()
