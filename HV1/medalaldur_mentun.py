import read_csv as data
import dict_sort
import matplotlib.pyplot as plt
import list_to_int as lti
import numpy as np

# Hver er meðalaldur háskólamenntaðs fólks, bæði karla og kvenna?

Mentun_ar = ('20 til 24 ára','25 til 29 ára','30 til 49 ára','50 til 64 ára','65 til 74 ára')
KynFlokkur = ('Alls','Karlar','Konur')
AllsMentun = {}

for kyn in range(len(KynFlokkur)):
	for x in range (len(Mentun_ar)):
		for row in data.menntun:
		    if row['Kyn'] == KynFlokkur[kyn] and row['Menntun'] == 'Háskólamenntun - ISCED 5, 6': 
		    	if row['Aldursflokkur/Búseta'] == Mentun_ar[x]:  
		      		row = dict_sort.key_sort(row)
		      		row = lti.tuple2_toint(row)
		      		AllsMentun[x] = row
		      		AllsMentun[Mentun_ar[x]] = AllsMentun.pop(x)


	x = np.zeros((len(Mentun_ar),len(AllsMentun[Mentun_ar[0]])))
	y = x.copy()

	for i in range(len(Mentun_ar)):
		for j in range(len(AllsMentun[(Mentun_ar[i])])):	
			x[i][j] = AllsMentun[Mentun_ar[i]][j][0]
			y[i][j] = AllsMentun[Mentun_ar[i]][j][1]

	for i in range(len(Mentun_ar)):
		plt.subplot(3,1,kyn+1)	
		plt.plot(x[i],y[i])
		plt.title('Aldursflokkar ({})/ menntun'.format(KynFlokkur[kyn]))

	plt.xlabel('Ár')
	plt.ylabel('Mannafjöldi')
	plt.legend((Mentun_ar),loc='upper right')
		
	plt.xlim(np.amin(x)-2, np.amax(x)+2)
	plt.ylim(np.amin(y)-1000,np.amax(y)+1000)
	plt.grid(True)


plt.tight_layout()
plt.show()

