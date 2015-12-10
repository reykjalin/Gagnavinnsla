import numpy as np
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from extract_from_export_all import export_sql
from extract_from_conflict import conflict


engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/lokaverkefni')


export_sql.to_sql('export', engine, if_exists='replace')
conflict.to_sql('conflict', engine, if_exists='replace')

