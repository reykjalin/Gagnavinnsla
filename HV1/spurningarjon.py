import read_csv as data

menntun = data.menntun
vinna = data.vinna

data.print_keys()

for row in menntun:
	for line in vinna:
		if row['Menntunarstig'] == 'Háskólamenntun - ISCED 5, 6' and line['Vinnuhlutfall'] == 'Regluleg laun - alls Meðaltal':
			print(row)
