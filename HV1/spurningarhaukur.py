import read_csv as data
import matplotlib.pyplot as mp
import dict_sort as ds
import list_to_int as i
import numpy

def innanh_vs_utanh():
	pass
	lol = ['Konur','Karlar']

	for illad in range(2):
		test = dict()
		input1 = lol[illad]
		for row in data.menntun:
			if row['Kyn'] == input1 and row['Aldursflokkur/Búseta'] == 'Höfuðborgarsvæði 16-74 ára':
				if row['Menntun'] == 'Háskólamenntun - ISCED 5, 6':
					test = row
				
		test = ds.key_sort(test)
		test = test[:-3]


		hello = i.tuple2_toint(test)


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

		avhas = numpy.mean(has)
		avall = numpy.mean(allir)
		avhasland = numpy.mean(hasland)
		avallirland = numpy.mean(allirland)



		plot1 = avhas/avall
		plot2 = avhasland/avallirland

		print(plot1*100, ' prósent innan höfuðborgarsvæðisins fá sé háskólamenntun ')
		print(plot2*100, ' prósent utan höfuðborgarsvæðisins fá sé háskólamenntun ')

		plot = [plot1,plot2]
		xas = [1,2]
		label = ["Innan höfuðborgarsvæðisins","Utan höfuðborgarsvæðisins"]
		title = [' Prósentumunur á konum sem fá sé Háskólamenntun innan og utan höfuðborgarsvæðis',' Prósentumunur á körlum sem fá sé Háskólamenntun innan og utan höfuðborgarsvæðis']

		mp.figure(illad+6)
		mp.bar(xas, plot, align = 'center')
		mp.title(title[illad])
		mp.xticks(xas, label)
		mp.xlim(0,3)
	

