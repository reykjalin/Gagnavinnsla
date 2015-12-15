# install sqlalchemy module
import numpy as np
import psycopg2
import pandas as pd
import getpass
from sqlalchemy import create_engine

from extract_from_export_all import export_sql, schema_export
from extract_from_conflict import conflict, schema_conflict
from extract_from_eclipse import eclipse, schema_eclipse
from extract_from_conflicts_loactions_coords import conflict_location_cords, schema_conflict_location_cords
from extract_from_eclipse_loactions_coords import eclipse_location_cords, schema_eclipse_location_cords

def sql_create_database(user_name, password, name_of_database, host):

	engine2 = create_engine('postgresql+psycopg2://{}:{}@{}:5432' .format(user_name,password,host))
	connection2 = engine2.connect()
	connection2.execute("commit")
	connection2.execute('create database {};' .format(name_of_database))
	connection2.close()
	print('Database: {}, has been created' .format(name_of_database))

def sql_populate_database(user_name, password, name_of_database,host):

	engine = create_engine('postgresql+psycopg2://{}:{}@{}:5432/{}' .format(user_name,password,host,name_of_database))
	connection = engine.connect()
	print('Connected')
	print('Creating tables')
	connection.execute(schema_eclipse)
	print('...')
	connection.execute(schema_conflict)
	print('...')
	connection.execute(schema_export)
	print('...')
	connection.execute(schema_conflict_location_cords)
	print('...')
	connection.execute(schema_eclipse_location_cords)
	print('Tabels created')
	connection.close()

	print('Populating tables')
	export_sql.to_sql('export', engine, if_exists='replace')
	print('...')
	conflict.to_sql('conflict', engine, if_exists='replace')
	print('...')
	eclipse.to_sql('eclipse', engine, if_exists='replace')
	print('...')
	conflict_location_cords.to_sql('conflictlc', engine, if_exists='replace')
	print('...')
	eclipse_location_cords.to_sql('eclipselc', engine, if_exists='replace')	
	print('Done!')

	return engine
