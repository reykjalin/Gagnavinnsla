import read_csv as data
import dict_sort
import list_to_int as lti
import matplotlib.pyplot as plot

menntun = data.menntun
data.print_keys()

Konur = dict()
Karlar = dict()

Ment = 'Háskólamenntun - ISCED 5, 6'
Ald = '16 til 74 ára'

for row in menntun:
	if row['Menntun'] == Ment and row ['Aldursflokkur/Búseta'] == Ald and row['Kyn'] == 'Karlar' :
		Karlar = row

for row in menntun:
	if row['Menntun'] == 'Háskólamenntun - ISCED 5, 6' and row ['Aldursflokkur/Búseta'] == '16 til 74 ára' and row['Kyn'] == 'Konur' :
		Konur = row

Karlar = dict_sort.key_sort(Karlar)
Konur = dict_sort.key_sort(Konur)

try:
	Karlar = lti.tuple2_toint(Karlar)
	Konur = lti.tuple2_toint(Konur)

except:
	pass

print(Karlar)
print('----------')
print(Konur)

ArKK = list()
FjKK = list()
ArKvK = list()
FjKvK = list()


for x,y in Karlar:
	ArKK.append(x)
	FjKK.append(y)

for z,k in Konur:
	ArKvK.append(z)
	FjKvK.append(k)


plot.plot(ArKK, FjKK)
plot.title(Ment)
plot.xticks([year for year in ArKK])
plot.xlim(min(ArKK)-1, max(ArKK)+1)

plot.plot(ArKvK, FjKvK)
plot.legend(('Karlar','Konur'))
plot.show()

