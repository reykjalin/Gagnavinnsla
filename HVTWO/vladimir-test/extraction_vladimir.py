import numpy as np
import pandas as pd


MoviesDatabse = pd.read_csv('movies.csv',sep = ',', encoding='UTF-8')
MoviesDatabse['year']= MoviesDatabse ['title'].str.extract('(\d\d\d\d)')
MoviesDatabse['title'] = [i.rsplit('(',1)[0].strip() for i in MoviesDatabse['title']]

MoviesLinks = pd.read_csv('links.csv',sep = ',', encoding='UTF-8')

MoviesRatings = pd.read_csv('ratings.csv',sep = ',', encoding='UTF-8')
MoviesRatings = MoviesRatings.drop('timestamp', 1)
MoviesRatings = MoviesRatings.sort(columns='movieId')


MoviesTags = pd.read_csv('tags.csv',sep = ',', encoding='UTF-8')
MoviesTags = MoviesTags.drop('timestamp', 1)

# MoviesMerge = pd.concat([MoviesDatabse, MoviesLinks], axis=1)

print(MoviesRatings.sort(columns='movieId'))

# theyear = [int(i.rsplit('(',1)[1].rstrip(')')) for i in MoviesDatabse.title]


# print(MoviesDatabse.head())
# print(MoviesLinks.head())
# print(MoviesRatings.head())
# print(MoviesTags.head())


# MoviesMerge = MoviesDatabse.append(MoviesLinks)
MoviesMerge = pd.concat([MoviesDatabse, MoviesLinks, MoviesRatings, MoviesTags], axis=1)
MoviesMerge.to_csv('test.csv', sep=',', encoding='utf-8')