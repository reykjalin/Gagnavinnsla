import numpy as np
import pandas as pd



MoviesDatabse = pd.read_csv('movies.csv',sep = ',', encoding='UTF-8',index_col='movieId')
MoviesDatabse['year']= MoviesDatabse ['title'].str.extract('(\d\d\d\d)')
MoviesDatabse['title'] = [i.rsplit('(',1)[0].strip() for i in MoviesDatabse['title']]

MoviesLinks = pd.read_csv('links.csv',sep = ',', encoding='UTF-8',index_col='movieId')

MoviesRatings = pd.read_csv('ratings.csv',sep = ',', encoding='UTF-8')
MoviesRatings = MoviesRatings.drop('timestamp', 1)
MoviesRatings.index.name = 'indexRating'


MoviesTags = pd.read_csv('tags.csv',sep = ',', encoding='UTF-8')
MoviesTags = MoviesTags.drop('timestamp', 1)
MoviesTags.index.name = 'indexTags'

