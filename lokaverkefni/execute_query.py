import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

def run_query(engine,column,table,where = '',group_by= '',order_by= ''):	
	connection = engine.connect()
	result = connection.execute("""select {} 
		from table {} 
		{}
		{}
		{}
		;""")
	}
	connection.close()
	return result

	