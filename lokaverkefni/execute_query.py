import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

def run_query(engine):
	connection = engine.connect()
	result = connection.execute("commit")
	connection.close()
	return result

	