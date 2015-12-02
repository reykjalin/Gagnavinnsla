import read_csv as data
import dict_sort
import matplotlib.pyplot as plt
import list_to_int as lti



# Hver er meðalaldur háskólamenntaðs fólks, bæði karla og kvenna?


Mentun_ar = ('20 til 24 ára','25 til 29 ára','30 til 49 ára','50 til 64 ára','65 til 74 ára')
AllsMentun = dict()
KarlaMentun = dict()
KvennaMentun = dict()


for x in range (len(Mentun_ar)):
	for row in data.menntun:
	    if row['Kyn'] == 'Alls' and row['Menntun'] == 'Háskólamenntun - ISCED 5, 6': 
	    	if row['Aldursflokkur/Búseta'] == Mentun_ar[x]:  
	      		row = dict_sort.key_sort(row)
	      		row = lti.tuple2_toint(row)
	      		AllsMentun[x] = row
	      		AllsMentun[Mentun_ar[x]] = AllsMentun.pop(x)
print(AllsMentun)	





