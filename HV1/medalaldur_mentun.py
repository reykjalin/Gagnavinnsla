import read_csv as data
import dict_sort
import matplotlib.pyplot as plt
import list_to_int as lti
import numpy as np





# Hver er meðalaldur háskólamenntaðs fólks, bæði karla og kvenna?

Mentun_ar = ('20 til 24 ára','25 til 29 ára','30 til 49 ára','50 til 64 ára','65 til 74 ára')

AllsMentun = {}
KarlaMentun = {}
KvennaMentun = {}

# Allir

for x in range (len(Mentun_ar)):
	for row in data.menntun:
	    if row['Kyn'] == 'Alls' and row['Menntun'] == 'Háskólamenntun - ISCED 5, 6': 
	    	if row['Aldursflokkur/Búseta'] == Mentun_ar[x]:  
	      		row = dict_sort.key_sort(row)
	      		row = lti.tuple2_toint(row)
	      		AllsMentun[x] = row
	      		AllsMentun[Mentun_ar[x]] = AllsMentun.pop(x)


x = np.zeros((len(Mentun_ar),len(AllsMentun[Mentun_ar[0]])))
y = x.copy()

for bla1 in range(len(Mentun_ar)):
	for bla2 in range(len(AllsMentun[(Mentun_ar[bla1])])):	
		x[bla1][bla2] = AllsMentun[Mentun_ar[bla1]][bla2][0]
		y[bla1][bla2] = AllsMentun[Mentun_ar[bla1]][bla2][1]

for i in range(len(Mentun_ar)):
	plt.plot(x[i],y[i])
	plt.title('Aldursflokkar (Allir)/ menntun')

plt.figure(1)	
plt.xlabel('Ár')
plt.ylabel('Mannafjöldi')
plt.legend((Mentun_ar),loc='upper right')
plt.xlim(np.amin(x)-2, np.amax(x)+2)
plt.ylim(np.amin(y)-1000,np.amax(y)+1000)
plt.grid(True)
AllsMentun.clear()

# Karlar

for x in range (len(Mentun_ar)):
	for row in data.menntun:
	    if row['Kyn'] == 'Karlar' and row['Menntun'] == 'Háskólamenntun - ISCED 5, 6': 
	    	if row['Aldursflokkur/Búseta'] == Mentun_ar[x]:  
	      		row = dict_sort.key_sort(row)
	      		row = lti.tuple2_toint(row)
	      		AllsMentun[x] = row
	      		AllsMentun[Mentun_ar[x]] = AllsMentun.pop(x)


x = np.zeros((len(Mentun_ar),len(AllsMentun[Mentun_ar[0]])))
y = x.copy()

for bla1 in range(len(Mentun_ar)):
	for bla2 in range(len(AllsMentun[(Mentun_ar[bla1])])):	
		x[bla1][bla2] = AllsMentun[Mentun_ar[bla1]][bla2][0]
		y[bla1][bla2] = AllsMentun[Mentun_ar[bla1]][bla2][1]

for i in range(len(Mentun_ar)):
	plt.plot(x[i],y[i])
	plt.title('Aldursflokkar (Karlar) / menntun')

plt.figure(2)	
plt.xlabel('Ár')
plt.ylabel('Mannafjöldi')
plt.legend((Mentun_ar),loc='upper right')
plt.xlim(np.amin(x)-2, np.amax(x)+2)
plt.ylim(np.amin(y)-1000,np.amax(y)+1000)
plt.grid(True)
AllsMentun.clear()

# Konur

for x in range (len(Mentun_ar)):
	for row in data.menntun:
	    if row['Kyn'] == 'Konur' and row['Menntun'] == 'Háskólamenntun - ISCED 5, 6': 
	    	if row['Aldursflokkur/Búseta'] == Mentun_ar[x]:  
	      		row = dict_sort.key_sort(row)
	      		row = lti.tuple2_toint(row)
	      		AllsMentun[x] = row
	      		AllsMentun[Mentun_ar[x]] = AllsMentun.pop(x)


x = np.zeros((len(Mentun_ar),len(AllsMentun[Mentun_ar[0]])))
y = x.copy()

for bla1 in range(len(Mentun_ar)):
	for bla2 in range(len(AllsMentun[(Mentun_ar[bla1])])):	
		x[bla1][bla2] = AllsMentun[Mentun_ar[bla1]][bla2][0]
		y[bla1][bla2] = AllsMentun[Mentun_ar[bla1]][bla2][1]

for i in range(len(Mentun_ar)):
	plt.plot(x[i],y[i])
	plt.title('Aldursflokkar (Konur) / menntun')

plt.figure(3)	
plt.xlabel('Ár')
plt.ylabel('Mannafjöldi')
plt.legend((Mentun_ar),loc='upper right')
plt.xlim(np.amin(x)-2, np.amax(x)+2)
plt.ylim(np.amin(y)-1000,np.amax(y)+1000)
plt.grid(True)
AllsMentun.clear()


plt.show()

