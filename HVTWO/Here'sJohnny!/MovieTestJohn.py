import csv
import numpy as np
import pandas as pd
import random as r
import pprint
import webbrowser

def newDict(x):
	count = 0
	NewDict = {}
	for i in x:
		NewDict[i] = x[x.columns[count]]
		count +=1
	return NewDict


# Information on movies
movies = pd.read_csv('movies.csv')
#print(movies.columns)
MovieDict = newDict(movies)

MovieDict['year']= movies['title'].str.extract('(\d\d\d\d)')
MovieDict['title'] = pd.Series([i.rsplit('(',1)[0].rstrip(')') for i in MovieDict['title']])


# Information on ratings and users
ratings = pd.read_csv('ratings.csv')
#print(ratings.columns)
RatingDict = newDict(ratings)


tags = pd.read_csv('tags.csv')
#print(tags.columns)
TagDict = newDict(tags)


# Movie-links
links = pd.read_csv('links.csv')
#print(links.columns)
LinkDict = newDict(links)

new = 2 # open in a new tab, if possible
#open a public URL, in this case, the webbrowser docs
url = "http://www.imdb.com/title/tt" + str(LinkDict['imdbId'][0])
#webbrowser.open(url,new=new)		# Uncomment to open browser with movie



