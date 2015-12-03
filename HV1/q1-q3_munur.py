import read_csv as data
import matplotlib.pyplot as mp
import dict_sort as ds
import list_to_int as i
import numpy 

def average_and_std_laun():
	pass
	test = dict()

	for row in data.vinna:
		if row['Kyn'] == 'Alls' and row['Starfsstétt'] == 'Alls':
			test[row['Ár']] = row['Heildarlaun - fullvinnandi Efri fjórðungsmörk'],row['Heildarlaun - fullvinnandi Neðri fjórðungsmörk']

	q1 = list()
	q3 = list()

	test = ds.key_sort(test)

	print('-------------------------q1-------------------------')
	for q,(w,e) in test:
		q1.append(e)
		q3.append(w)

	q1 = i.toint(q1)
	q3 = i.toint(q3)
	q1.sort()
	q3.sort() # just cuz I caann

	print(q1)
	print('---------------------------------------------------')
	print(q3)

	listq1 = numpy.array(q1)
	stdevq1 = listq1.std()
	listq3 = numpy.array(q3)
	stdevq3 = listq3.std()

	avnedri = numpy.mean(q1)
	avefri  = numpy.mean(q3)

	print()
	print(stdevq1,stdevq3,avnedri,avefri)

	prosq1 = stdevq1/avnedri
	prosq3 = stdevq3/avefri
	prosfact = avefri/avnedri
	prosstd = stdevq3/stdevq1


	plot1 = [prosq1,prosq3]
	plot2 = [prosfact,prosstd]
	x = [1,2]
	label = ["Neðri fjórðungsmörk","Efri fjórðungsmörk"]
	label1 = ['Hlutfall milli meðaltals','Hlutfall milli Staðalfráviks']

	mp.figure(8)
	mp.subplot(2,1,2)
	mp.bar(x,plot1,align = 'center')
	mp.title('Prósentutala Staðalfráviks á meðaltali ')
	mp.xlim(0,3)
	mp.xticks(x,label)

	mp.subplot(2,1,1)
	mp.bar(x,plot2,align = 'center')
	mp.title('Samanburður á meðaltali og Staðalfráviki')
	mp.xticks(x,label1)
	mp.xlim(0,3)



