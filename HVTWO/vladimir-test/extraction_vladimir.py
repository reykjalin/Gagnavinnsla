import numpy as np
import pandas as pd

MoviesDatabse = pd.read_csv('movies.csv',sep = ',', encoding='UTF-8')
MoviesDatabse['year']= MoviesDatabse ['title'].str.extract('(\d\d\d\d)')
MoviesDatabse['title'] = [i.rsplit('(',1)[0].strip() for i in MoviesDatabse['title']]
MoviesDatabse.columns = map(str.lower, MoviesDatabse.columns)

MoviesLinks = pd.read_csv('links.csv',sep = ',', encoding='UTF-8')
MoviesLinks.columns = map(str.lower, MoviesLinks.columns)

MoviesRatings = pd.read_csv('ratings.csv',sep = ',', encoding='UTF-8')
MoviesRatings = MoviesRatings.drop('timestamp', 1)
MoviesRatings.index.name = 'indexRating'
MoviesRatings.columns = map(str.lower, MoviesRatings.columns)

MoviesTags = pd.read_csv('tags.csv',sep = ',', encoding='UTF-8')
MoviesTags = MoviesTags.drop('timestamp', 1)
MoviesTags.index.name = 'indexTags'
MoviesTags.columns = map(str.lower, MoviesTags.columns)

print(MoviesDatabse.head())