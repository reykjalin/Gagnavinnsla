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


# average rating
# select m.title, avg(r.rating) as average  
# from ratings r, movies m
# where m.movieid = r.movieid
# group by m.title
# order by m.title;

# select m.title, m.year, avg(r.rating) as average ,sum(r.userid)
# from ratings r, movies m
# where m.movieid = r.movieid
# group by m.title, m.year 
# order by average desc, m.year desc;

# select m.title, m.year, avg(r.rating) as average ,sum(r.userid) as number_of_users_voted, m.genres
# from ratings r, movies m
# where m.movieid = r.movieid 
# and lower(m.genres) like '%action%' and lower(m.genres) like '%sci%' and lower(m.genres) like '%dra%' and lower(m.genres) like '%%'
# group by m.title, m.year, m.genres 
# order by average desc, m.year desc;

# select m.title, m.year, avg(r.rating) as average ,count(r.userid) as number_of_users_voted, m.genres, t.tag 
# from ratings r, movies m, tags t
# where m.movieid = r.movieid and m.movieid = t.movieid
# and lower(m.genres) like '%action%' and lower(m.genres) like '%sci%' and lower(m.genres) like '%dra%' and lower(m.genres) like '%%'
# group by m.title, m.year, m.genres, t.tag 
# order by average desc, m.year desc;