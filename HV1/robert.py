import read_csv as data
import dict_sort as ds
import matplotlib.pyplot as plt
import list_to_int as lt


def tuple2_tofloat(l):
    newl = list()
    for x,y in l:
        try:
            newl.append((float(x),float(y)))
        except:
            pass
    return newl


KK = dict()

for row in data.vinna:
	if row['Starfsstétt'] == 'Sérfræðingar' and row['Kyn'] == 'Karlar':
		KK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']

print('KK 1:',KK)
KK = ds.key_sort(KK)
print('KK 2:',KK)
#IKK = lt.tuple2_toint(KK)
IKK = tuple2_tofloat(KK)
print('KK 3:', IKK)

x = list()
y = list()

for i in range(len(IKK)):
	x.append(IKK[i][0])
	y.append(IKK[i][1])


plt.plot(x,y)
plt.xticks([year for year in x])
plt.show()

print()
print()
data.print_keys()


