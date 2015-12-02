import read_csv as data
import dict_sort as ds
import matplotlib.pyplot as plt
import list_to_int as lt
import plotter 


KK = dict()

for row in data.vinna:
	if row['Starfsstétt'] == 'Sérfræðingar' and row['Kyn'] == 'Karlar':
		KK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']

print('KK 1:',KK)
KK = ds.key_sort(KK)
print('KK 2:',KK)
IKK = lt.tuple2_toint(KK)
print('KK 3:', IKK)

x = list()
y = list()

for i in range(len(IKK)):
	x.append(KK[i][0])
	y.append(KK[i][1])


plt.plot(x,y)
plt.xticks([year for year in x])
plt.show()

print()
print()
data.print_keys()


