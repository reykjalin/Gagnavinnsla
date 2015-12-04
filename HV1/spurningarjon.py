
# Er munur á fjölda útskrifta úr háksóla eftir kynjum?
import read_csv as data
import dict_sort
import list_to_int as lti
import matplotlib.pyplot as plot

# Uncomment til að sjá alla keys sem hægt er að nota
#data.print_keys()

Konur = dict(); Karlar = dict()

#Breytur sem fara inn í plot
Ment = 'Háskólamenntun - ISCED 5, 6'
Ald = '16 til 74 ára'

for row in data.menntun:
	if row['Menntun'] == Ment and row ['Aldursflokkur/Búseta'] == Ald and row['Kyn'] == 'Karlar':
		Karlar = row

for row in data.menntun:
	if row['Menntun'] == Ment and row ['Aldursflokkur/Búseta'] == Ald and row['Kyn'] == 'Konur':
		Konur = row

# Flokka dictionary eftir lyklum
Karlar = dict_sort.key_sort(Karlar)
Konur = dict_sort.key_sort(Konur)

# Breyta tuple í int
Karlar = lti.tuple2_toint(Karlar)
Konur = lti.tuple2_toint(Konur)

ArKK = list(); FjKK = list(); ArKvK = list(); FjKvK = list(); Fj = list()

# Setja int í lista
for x,y in Karlar:
	ArKK.append(x)
	FjKK.append(y)

for z,k in Konur:
	ArKvK.append(z)
	FjKvK.append(k)

# Summa af körlum og konum
Fj = [x + y for x, y in zip(FjKK, FjKvK)]

# Plot commentað út því það er gert í aðalskrá
# plot.plot(ArKK, FjKK)
# plot.title(str.join('\n', (Ment,Ald)))
# plot.xticks([year for year in ArKK])
# plot.xlabel('Ár')
# plot.ylabel('Fjöldi')
# plot.plot(ArKvK,FjKvK)
# plot.plot(ArKK, Fj)
# plot.legend(('Karlar','Konur','Heild'),loc='lower right')
# plot.xlim(min(ArKK)-0.5, max(ArKK)+0.5)
# plot.ylim(0,max(Fj)+1000)

# plot.show()

