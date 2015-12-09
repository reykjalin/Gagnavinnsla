import pandas as pd
import pprint as pp


############################## Column names for dataframes ##############################
mcols = ['movieId', 'title', 'genres']
rcols = ['userId', 'movieId', 'rating', 'timestamp']
tcols = ['userId', 'movieId', 'tag', 'timestamp']
############################## Column names for dataframes ##############################


############################## Read data from dat files ##############################
movies = pd.read_csv('../ml-10M100K/movies.dat', sep = '::', names = mcols, engine = 'python', keep_default_na = False)
#links = pd.read_csv('../ml-10M100K/links.csv', engine = 'python')
ratings = pd.read_csv('../ml-10M100K/ratings.dat', sep = '::', names = rcols, engine = 'python', keep_default_na = False)
tags = pd.read_csv('../ml-10M100K/tags.dat', sep = '::', names = tcols, engine = 'python', keep_default_na = False)
############################## Read data from dat files ##############################


############################## Fix indexes and add column keys ##############################
movies.set_index('movieId', inplace = True)
ratings.set_index('movieId', inplace = True)
tags.set_index('movieId', inplace = True)
############################## Fix indexes and add column keys ##############################


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


############################## Create tag sets ##############################
tmdict = {}
for i in tags.index:
    tlist = tags[tags.index == i].values
    for t in tlist:
        if i not in tmdict.keys():
            tmdict[i] = [t[1],]
        else:
            tmdict[i].append(t[1])
for k in tmdict.keys():
    tmdict[k] = set(tmdict[k])
############################## Create tag sets ##############################


############################## Create sql commands ##############################
outs = open('insert_to_movielens.sql', 'w')

for i in movies.index:
    mov = movies[movies.index == i].values[0]
    outs.write("insert into movies (id, title, year, rating) values ('{}', '{}', '{}', {})\n".format(i, mov[0].replace("'", "''"), mov[1], mov[3]))

for i in set(ratings.index):
    rlist = ratings[ratings.index == i].values
    for r in rlist:
        outs.write("insert into ratings (movieid, userid, rating) values ('{}', '{}', {})\n".format(i, r[0], r[1]))

# for i in links.index:
#     l = links[links.index == i].values[0]
#     outs.write("insert into links (movieid, imdbid, tmdbid) values ('{}', '{}', '{}')\n".format(i, l[0], l[1]))

for i in set(tags.index):
    tlist = tags[tags.index == i].values
    for t in tlist:
        outs.write("insert into tags (movieid, userid, tag) values ('{}', '{}', '{}')\n".format(i, t[0], t[1].replace("'", "''")))

for i in genres.keys():
    glist = genres[i]
    for g in glist:
        outs.write("insert into genres (genre, movieid) values ('{}', '{}')\n".format(i, g))

for i in tmdict.keys():
    tlist = tmdict[i]
    for t in tlist:
        outs.write("insert into mtags (movieid, tag) values ('{}', '{}')\n".format(i, t.replace("'", "''")))

outs.close()
############################## Create sql commands ##############################
