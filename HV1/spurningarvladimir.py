import read_csv as data
import dict_sort
import matplotlib.pyplot as plt
import list_to_int as lti
import numpy as np


from read_csv import menntun_menntun


def aldurshop_mentun():
	# define parameters
	Mentun_ar = ('20 til 24 ára','25 til 29 ára','30 til 49 ára','50 til 64 ára','65 til 74 ára')
	menntun_kyn = ('Karlar','Konur')
	AllsMentun = {}

	# pick data and plot multiple plots on multiple figures
	for menntun in range (len(menntun_menntun)):
		for kyn in range(len(menntun_kyn)):
			for ar in range (len(Mentun_ar)):
				for row in data.menntun:
				    if row['Kyn'] == menntun_kyn[kyn] and row['Menntun'] == menntun_menntun[menntun]: 
				    	if row['Aldursflokkur/Búseta'] == Mentun_ar[ar]:
				    	  	#removing unwanted parameters and leaving only ejeccational level 
				      		row = dict_sort.key_sort(row)
				      		row = lti.tuple2_toint(row)
				      		AllsMentun[ar] = row
				      		AllsMentun[Mentun_ar[ar]] = AllsMentun.pop(ar)

			# creating 2 dimenational parameters for x and y axis for each age group
			# x-year, y-amount
			x = np.zeros((len(Mentun_ar),len(AllsMentun[Mentun_ar[0]]))) 
			y = x.copy()
			# copying parameters for x and y axis
			for i in range(len(Mentun_ar)):
				for j in range(len(AllsMentun[(Mentun_ar[i])])):	
					x[i][j] = AllsMentun[Mentun_ar[i]][j][0]
					y[i][j] = AllsMentun[Mentun_ar[i]][j][1]
			# download parameters for plloting grpahs  	
			for i in range(len(Mentun_ar)):
				plt.figure(menntun)
				plt.subplot(2,1,kyn+1)	
				plt.plot(x[i],y[i])
				plt.title('Aldursflokkar ({})/ menntun: {}'.format(menntun_kyn[kyn],menntun_menntun[menntun]))

			plt.xlabel('Ár')
			plt.ylabel('Mannafjöldi')
			plt.legend((Mentun_ar),loc='upper right')
				
			plt.xlim(np.amin(x)-2, np.amax(x)+2)
			plt.ylim(np.amin(y)-1000,np.amax(y)+1000)
			plt.grid(True)
			plt.tight_layout()

	




