import read_csv as data
import dict_sort as ds
import matplotlib.pyplot as plt
import list_to_float as fl
#---------------------------bý til dict------------------------
Allir = dict()
KK = dict()
KVK = dict()

SkrifstofaAllir = dict()
SkrifstofaKK = dict()
SkrifstofaKVK = dict()

SerfrAllir = dict()
SerfrKK = dict()
SerfrKVK = dict()

StjoAllir = dict()
StjoKK = dict()
StjoKVK = dict()

#-------------------------------------Filter gögnin -------------------------------------
for row in data.vinna:
	if row['Starfsstétt'] == 'Alls':
		if row['Kyn'] == 'Alls':
			Allir[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Karlar':
			KK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Konur':
			KVK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']

	elif row['Starfsstétt'] == 'Skrifstofufólk':
		if row['Kyn'] == 'Alls':
			SkrifstofaAllir[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Karlar':
			SkrifstofaKK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Konur':
			SkrifstofaKVK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']

	elif row['Starfsstétt'] == 'Sérfræðingar':
		if row['Kyn'] == 'Alls':
			SerfrAllir[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Karlar':
			SerfrKK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Konur':
			SerfrKVK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']

	if row['Starfsstétt'] == 'Sjórnendur':
		if row['Kyn'] == 'Alls':
			StjoAllir[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Karlar':
			StjoKK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']
		elif row['Kyn'] == 'Konur':
			StjoKVK[row['Ár']] = row['Greiddar stundir - fullvinnandi Meðaltal']

#--------------------------------Sorta dict og bý til lista---------------------------------------
print('Allir: ', StjoAllir)
print('KK: ', StjoKK)
print('KVK: ', StjoKVK)

Allir = ds.key_sort(Allir)
KK = ds.key_sort(KK)
KVK = ds.key_sort(KVK)

SkrifstofaAllir = ds.key_sort(SkrifstofaAllir)
SkrifstofaKK = ds.key_sort(SkrifstofaKK)
SkrifstofaKVK = ds.key_sort(SkrifstofaKVK)

SerfrAllir = ds.key_sort(SerfrAllir)
SerfrKK = ds.key_sort(SerfrKK)
SerfrKVK = ds.key_sort(SerfrKVK)

StjoAllir = ds.key_sort(StjoAllir)
StjoKK = ds.key_sort(StjoKK)
StjoKVK = ds.key_sort(StjoKVK)

#----------------------------------Breyti listanum í float-------------------------------------------
Allir = fl.tuple2_tofloat(Allir)
KK = fl.tuple2_tofloat(KK)
KVK = fl.tuple2_tofloat(KVK)

SkrifstofaAllir = fl.tuple2_tofloat(SkrifstofaAllir)
SkrifstofaKK = fl.tuple2_tofloat(SkrifstofaKK)
SkrifstofaKVK = fl.tuple2_tofloat(SkrifstofaKVK)

SerfrAllir = fl.tuple2_tofloat(SerfrAllir)
SerfrKK = fl.tuple2_tofloat(SerfrKK)
SerfrKVK = fl.tuple2_tofloat(SerfrKVK)

StjoAllir = fl.tuple2_tofloat(StjoAllir)
StjoKK = fl.tuple2_tofloat(StjoKK)
StjoKVK = fl.tuple2_tofloat(StjoKVK)

#---------------------------------------Bý til lista ------------------------------------
# Allir 
xA = list()
yA = list()
xK = list()
yK = list()
xKV = list()
yKV = list()

# Skrifstofa
xSKA = list()
ySKA = list()
xSKK = list()
ySKK = list()
xSKV = list()
ySKV = list()
#Sérfræðingar
xSerKA = list()
ySerKA = list()
xSerKK = list()
ySerKK = list()
xSerKV = list()
ySerKV = list()
# Stjórnendur
xStjoA = list()
yStjoA = list()
xStjoKK = list()
yStjoKK = list()
xStjoKV = list()
yStjoKV = list()
#-------------------------------------------Skipti gögnunum í tvennt----------------------------------
for i in range(len(Allir)):
	xA.append(Allir[i][0])
	yA.append(Allir[i][1])

for i in range(len(KK)):
	xK.append(KK[i][0])
	yK.append(KK[i][1])

for i in range(len(KVK)):
	xKV.append(KVK[i][0])
	yKV.append(KVK[i][1])
#---------------------------
for i in range(len(SkrifstofaAllir)):
	xSKA.append(SkrifstofaAllir[i][0])
	ySKA.append(SkrifstofaAllir[i][1])

for i in range(len(SkrifstofaKK)):
	xSKK.append(SkrifstofaKK[i][0])
	ySKK.append(SkrifstofaKK[i][1])

for i in range(len(KVK)):
	xSKV.append(KVK[i][0])
	ySKV.append(KVK[i][1])
#---------------------------
for i in range(len(SerfrAllir)):
	xSerKA.append(SkrifstofaAllir[i][0])
	ySerKA.append(SkrifstofaAllir[i][1])

for i in range(len(SerfrKK)):
	xSerKK.append(SkrifstofaKK[i][0])
	ySerKK.append(SkrifstofaKK[i][1])

for i in range(len(SerfrKVK)):
	xSerKV.append(KVK[i][0])
	ySerKV.append(KVK[i][1])
#---------------------------
for i in range(len(StjoAllir)):
	xStjoA.append(Allir[i][0])
	yStjoA.append(Allir[i][1])

for i in range(len(StjoKK)):
	xStjoKK.append(KK[i][0])
	yStjoKK.append(KK[i][1])

for i in range(len(StjoKVK)):
	xStjoKV.append(KVK[i][0])
	yStjoKV.append(KVK[i][1])
#-----------------------------------------------------------------------------
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(xA,yA)
plt.xticks([year for year in xK])
plt.plot(xK,yK)
plt.plot(xKV,yKV)
plt.ylabel('Klukkutímar')
plt.title('Starfstétt- Allar')
plt.legend(('Allir','Karlar','Konur'))

plt.subplot(2,1,2)
plt.plot(xSKA,ySKA)
plt.xticks([year for year in xSKK])
plt.plot(xSKK,ySKK)
plt.plot(xSKV,ySKV)
plt.ylabel('Klukkutímar')
plt.title('Starfstétt- Skrifstofa')
plt.legend(('Allir','Karlar','Konur'))

# plt.figure(2)
# plt.subplot(2,1,1)
# plt.plot(xSerKA,ySerKA)
# plt.xticks([year for year in xSerKK])
# plt.plot(xSerKK,ySerKK)
# plt.plot(xSerKV,ySerKV)
# plt.ylabel('Klukkutímar')
# plt.title('Starfstétt- Sérfræðingar')
# plt.legend(('Allir','Karlar','Konur'))

# plt.subplot(2,1,2)
# plt.plot(xStjoA,yStjoA)
# plt.xticks([year for year in xStjoKK])
# plt.plot(xStjoKK,yStjoKK)
# plt.plot(xStjoKV,yStjoKV)
# plt.ylabel('Klukkutímar')
# plt.title('Starfstétt- Stjórnendur')
# plt.legend(('Allir','Karlar','Konur'))

plt.show()

print()
print()
data.print_keys()


