import pandas as pd
import pprint as pp

movies = pd.read_csv('../ml-latest-small/movies.csv', index_col = 'movieId')
links = pd.read_csv('../ml-latest-small/links.csv', index_col = 'movieId')
ratings = pd.read_csv('../ml-latest-small/ratings.csv', index_col = 'movieId')
tags = pd.read_csv('../ml-latest-small/tags.csv', index_col = 'movieId')


############################## Split year from movie titles ##############################
years = list()
for i in movies.index:
    title = movies[movies.index == i].title.values[0]
    title = title.rsplit('(', 1)
    if len(title) > 1:
        years.append(title[1].strip(')'))
    else:
        years.append('not specified')
    title = title[0].strip()
    movies.loc[i, 'title'] = title
movies['year'] = pd.Series(years, index = movies.index)
# Move year column to be after title
movies = movies.reindex_axis(['title', 'year', 'genres'], axis = 1)
############################## Split year from movie titles ##############################


############################## Add ratings to movies ##############################
avgr = []
for i in movies.index:
    r = ratings[ratings.index == i]['rating']
    if r.size > 0:
        avgr.append(r.sum() / r.size)
    else:
        avgr.append(0)

movies['rating'] = pd.Series(avgr, index = movies.index)
############################## Add ratings to movies ##############################


############################## Create genre dict ##############################
genres = {}
for i in movies.index:
    movie_genres = movies[movies.index == i]['genres'].values
    for genre_string in movie_genres:
        genre_string = genre_string.split('|')
        for g in genre_string:
            if g not in genres.keys():
                genres[g] = [i,]
            else:
                genres[g].append(i)
############################## Create genre dict ##############################


############################## Create sql commands ##############################
############################## Create sql commands ##############################
