import numpy as np
import psycopg2
import pandas as pd
import populate_sql as popsql
from execute_query import run_query
from sqlalchemy import create_engine


user_name = 'postgres'
password = 'postgres'
database_name = 'test_data'
host = 'localhost'

# popsql.sql_create_database(user_name,password ,database_name,host)

# engine = popsql.sql_populate_database(user_name,password ,database_name,host)
engine = create_engine('postgresql+psycopg2://{}:{}@{}:5432/{}' .format(user_name,password ,host,database_name))

# def run_query(engine,column,table,where = '',group_by= '',order_by= ''):	
result = run_query(engine, 'year, type', 'export',' where year > 1950','','order by year desc')
for row in result:
    print ("year is: {} {}" .format(row['year'],row['type']))




