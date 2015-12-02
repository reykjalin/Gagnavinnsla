import read_csv as data
import dict_sort
import matplotlib.pyplot as plt



# Hver er meðalaldur háskólamenntaðs fólks, bæði karla og kvenna?


Mentun_ar = ('20 til 24 ára','25 til 29 ára','30 til 49 ára','50 til 64 ára','65 til 74 ára')
AllsMentun = dict()
KarlaMentun = dict()
KvennaMentun = dict()


for x in range (len(Mentun_ar)):
	for row in data.menntun:
	    if row['Kyn'] == 'Alls' and row['Menntun'] == 'Háskólamenntun - ISCED 5, 6': 
	    	if row['Aldursflokkur/Búseta'] == Mentun_ar[x]:  
	      		AllsMentun[x] = row
	      		print (AllsMentun[x])
	      		print("-----------------")

	  		# if row['Aldursflokkur/Búseta'] == '25 til 29 ára':  
	    #   		AllsMentun_25_29 = row

	  		# if row['Aldursflokkur/Búseta'] == '30 til 49 ára':  
	    #   		print (row)
	  		# if row['Aldursflokkur/Búseta'] == '50 til 64 ára':  
	    #   		AllsMentun_50_64 = row
	  		# if row['Aldursflokkur/Búseta'] == '65 til 74 ára':  
	    #   		AllsMentun_65_74 = row


	print(type(AllsMentun))	




# AllsMentun = dict_sort.sort(AllsMentun)

# data.print_keys()

# for key, value in AllsMentun.items():
#   print(key, '-', value)

