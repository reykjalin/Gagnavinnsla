import numpy as np
import psycopg2
import pandas as pd
import populate_sql as popsql
import execute_query
from sqlalchemy import create_engine


user_name = 'postgres'
password = 'postgres'
database_name = 'test_data'

# popsql.sql_create_database(user_name,password ,database_name)

engine = popsql.sql_populate_database(user_name,password ,database_name)

# def run_query(engine,column,table,where = '',group_by= '',order_by= ''):	
result = 


