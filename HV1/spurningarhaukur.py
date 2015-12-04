import read_csv as data # Tek inn gögn frá read_csv python skránni
import matplotlib.pyplot as mp
import dict_sort as ds # skilgreining á sér föllum sem hópurinn bjó til
import list_to_int as i 
import numpy

def innanh_vs_utanh(): # svo hægt sé að vitna í þetta í öðrum skrám
	pass
	lol = ['Konur','Karlar'] # hvaða breytur á að skoða

	for illad in range(2):
		test = dict()
		input1 = lol[illad]
		for row in data.menntun:
			if row['Kyn'] == input1 and row['Aldursflokkur/Búseta'] == 'Höfuðborgarsvæði 16-74 ára': # hvaða breytur á að skoða við hvaða tilefni
				if row['Menntun'] == 'Háskólamenntun - ISCED 5, 6':
					test = row # skrifað inn í tímabundna skrá test
				
		test = ds.key_sort(test) # sorterað
		test = test[:-3] # teknir þeir dálkar af gögnunum sem ekki skipta máli


		hello = i.tuple2_toint(test) # gögnum breytt í tölur af gerð int


		for row in data.menntun:
			if row['Kyn'] == input1 and row['Aldursflokkur/Búseta'] == 'Höfuðborgarsvæði 16-74 ára':
				if row['Menntun'] == 'Alls':
					test = row


		test = ds.key_sort(test)
		test = test[:-3]

		hello1 = i.tuple2_toint(test)


		for row in data.menntun:
			if row['Kyn'] == input1 and row['Aldursflokkur/Búseta'] == 'Utan höfuðborgarsvæðis 16-74 ára':
				if row['Menntun'] == 'Háskólamenntun - ISCED 5, 6':
					test = row
				
		test = ds.key_sort(test)
		test = test[:-3]


		hello2 = i.tuple2_toint(test)


		for row in data.menntun:
			if row['Kyn'] == input1 and row['Aldursflokkur/Búseta'] == 'Utan höfuðborgarsvæðis 16-74 ára':
				if row['Menntun'] == 'Alls':
					test = row


		test = ds.key_sort(test)
		test = test[:-3]

		hello3 = i.tuple2_toint(test)

		# viss gögn vinsuð úr inní eftirfarandi breytur

		x = list()
		has = list()
		allir = list()
		hasland = list()
		allirland = list()

		for key, value in hello:
			x.append(key)
			has.append(value)

		for key, value in hello1:
			allir.append(value)

		for key, value in hello2:
			hasland.append(value)

		for key, value in hello3:
			allirland.append(value)

		avhas = numpy.mean(has)# meðaltal fundið
		avall = numpy.mean(allir)
		avhasland = numpy.mean(hasland)
		avallirland = numpy.mean(allirland)



		plot1 = avhas/avall # Hlutfall fundið
		plot2 = avhasland/avallirland
		plot = [plot1,plot2]
		xas = [1,2]
		label = ["Innan höfuðborgarsvæðisins","Utan höfuðborgarsvæðisins"]
		title = [' Prósentumunur á konum sem fá sé Háskólamenntun innan og utan höfuðborgarsvæðis',' Prósentumunur á körlum sem fá sé Háskólamenntun innan og utan höfuðborgarsvæðis']

		mp.figure(illad+6) # gögn plottuð upp sem bar graf, mynd 6 út af main skrá
		mp.bar(xas, plot, align = 'center')
		mp.title(title[illad])
		mp.xticks(xas, label)
		mp.xlim(0,3) # x ás cappaður í 0-3
	

