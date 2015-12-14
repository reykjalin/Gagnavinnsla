# install sqlalchemy module
import numpy as np
import psycopg2
import pandas as pd
import getpass
from sqlalchemy import create_engine

from extract_from_export_all import export_sql, schema_export
from extract_from_conflict import conflict, schema_conflict
from extract_from_eclipse import eclipse, schema_eclipse


def sql_create_database(user_name, password, name_of_database):

	engine2 = create_engine('postgresql+psycopg2://{}:{}@localhost:5432' .format(user_name,password))
	connection2 = engine2.connect()
	connection2.execute("commit")
	connection2.execute('create database {};' .format(name_of_database))
	connection2.close()
	print('Database: {}, has been created' .format(name_of_database))

def sql_populate_database(user_name, password, name_of_database):

	engine = create_engine('postgresql+psycopg2://{}:{}@localhost:5432/{}' .format(user_name,password,name_of_database))
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

	return engine
