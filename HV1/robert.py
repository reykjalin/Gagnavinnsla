import read_csv as data
import dict_sort as ds
import matplotlib.pyplot as plt
import list_to_float as fl
#-----------------------------------------------------------------------------
Allir = dict()
KK = dict()
KVK = dict()
#-----------------------------------------------------------------------------
for row in data.vinna:
	if row['Starfsstétt'] == 'Alls' and row['Kyn'] == 'Alls':
		Allir[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
	elif row['Starfsstétt'] == 'Alls' and row['Kyn'] == 'Karlar':
		KK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
	elif row['Starfsstétt'] == 'Alls' and row['Kyn'] == 'Konur':
		KVK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
#-----------------------------------------------------------------------------
Allir = ds.key_sort(Allir)
KK = ds.key_sort(KK)
KVK = ds.key_sort(KVK)
#-----------------------------------------------------------------------------
Allir = fl.tuple2_tofloat(Allir)
KK = fl.tuple2_tofloat(KK)
KVK = fl.tuple2_tofloat(KVK)
#-----------------------------------------------------------------------------
print('Allir: ', Allir)
print('KK: ',KK)
print('KVK: ', KVK)
#-----------------------------------------------------------------------------
xA = list()
yA = list()
xK = list()
yK = list()
xKV = list()
yKV = list()
#-----------------------------------------------------------------------------
for i in range(len(Allir)):
	xA.append(Allir[i][0])
	yA.append(Allir[i][1])

for i in range(len(KK)):
	xK.append(KK[i][0])
	yK.append(KK[i][1])

for i in range(len(KVK)):
	xKV.append(KVK[i][0])
	yKV.append(KVK[i][1])
#-----------------------------------------------------------------------------
plt.plot(xA,yA)
plt.xticks([year for year in xK])
plt.plot(xK,yK)
plt.plot(xKV,yKV)

plt.show()

print()
print()
data.print_keys()


