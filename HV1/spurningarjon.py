import read_csv as data
import dict_sort
import list_to_int as lti
import matplotlib.pyplot as plot

#data.print_keys()

Konur = dict(); Karlar = dict()

Ment = 'Háskólamenntun - ISCED 5, 6'				#Breytur sem fara inn í plot
Ald = '16 til 74 ára'

for row in data.menntun:
	if row['Menntun'] == Ment and row ['Aldursflokkur/Búseta'] == Ald and row['Kyn'] == 'Karlar':
		Karlar = row

for row in data.menntun:
	if row['Menntun'] == Ment and row ['Aldursflokkur/Búseta'] == Ald and row['Kyn'] == 'Konur':
		Konur = row

Karlar = dict_sort.key_sort(Karlar)
Konur = dict_sort.key_sort(Konur)

Karlar = lti.tuple2_toint(Karlar)
Konur = lti.tuple2_toint(Konur)

ArKK = list(); FjKK = list(); ArKvK = list(); FjKvK = list()

for x,y in Karlar:
	ArKK.append(x)
	FjKK.append(y)

for z,k in Konur:
	ArKvK.append(z)
	FjKvK.append(k)


plot.plot(ArKK, FjKK)
plot.title(str.join('\n', (Ment,Ald)))
plot.xticks([year for year in ArKK])
plot.xlabel('Ár')
plot.ylabel('Fjöldi brautskráðra')

plot.plot(ArKvK,FjKvK)
plot.legend(('Karlar','Konur'),loc='lower right')
plot.xlim(min(ArKK)-0.5, max(ArKK)+0.5)
plot.ylim(min(min(FjKK),min(FjKvK))-500,max(max(FjKK),max(FjKvK))+500)

plot.show()

