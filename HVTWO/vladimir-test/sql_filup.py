import numpy as np
import psycopg2
import pandas as pd
from extraction_vladimir import MoviesDatabse, MoviesLinks, MoviesRatings, MoviesTags 


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/vladimir')
MoviesDatabse.to_sql('movies', engine, if_exists='replace')
MoviesLinks.to_sql('links', engine, if_exists='replace')
MoviesRatings.to_sql('ratings', engine, if_exists='replace')
MoviesTags.to_sql('tags', engine, if_exists='replace')




