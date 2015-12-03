import numpy as np
import pandas as pd

data = {}
data['Movie'] = ['Alien','Se7en','Taxi','Ran']
data['Year'] = [1979,1995,1998,1985]
data['Dir'] = ['Scott','Fincher','Besson','Kurosawa']
data['Rating'] = [8.5, 8.7, 6.9, 8.3]

m = pd.DataFrame(data,columns = ['Year','Movie','Dir','Rating'])

print(m)

# Búa til nýjan csv file (engar gæsalappir utan um gildi)
#m.to_csv('movies.csv')

# Prenta út allar myndir gerðar 1985
print(m[m.Year == 1985])

# Prentar út bara ártalið þar sem það er 1985
print(m['Year'][m.Year == 1985])

# Prenta út 3ju línu
print(m['Year'][3])