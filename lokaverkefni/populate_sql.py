# install sqlalchemy module
import numpy as np
import psycopg2
import pandas as pd
import getpass
from extract_from_export_all import export_sql, schema_export
from extract_from_conflict import conflict, schema_conflict
from extract_from_eclipse import eclipse, schema_eclipse


from sqlalchemy import create_engine

un = input("Enter user name: ")
pw = getpass.getpass()
# nd2 = input("Main name of database: ")
nd = input("Name of database: ")




engine2 = create_engine('postgresql+psycopg2://{}:{}@localhost:5432' .format(un,pw))
connection2 = engine2.connect()
connection2.execute("commit")
connection2.execute('create database {};' .format(nd))
connection2.close()
print('Database: {}, has been created' .format(nd))


engine = create_engine('postgresql+psycopg2://{}:{}@localhost:5432/{}' .format(un,pw,nd))
connection = engine.connect()
print('Connected')
print('Creating tables')
connection.execute(schema_eclipse)
print('...')
connection.execute(schema_conflict)
print('...')
connection.execute(schema_export)
connection.close()

print('Populating tables')
export_sql.to_sql('export', engine, if_exists='replace')
print('...')
conflict.to_sql('conflict', engine, if_exists='replace')
print('...')
eclipse.to_sql('eclipse', engine, if_exists='replace')
print('Done!')
