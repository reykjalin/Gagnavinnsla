import read_csv as data
import dict_sort
import matplotlib.pyplot as plt

avg_all = dict()
avg_kvk = dict()
avg_kk = dict()

for row in data.vinna:
    if row['Starfsstétt'] == 'Alls':
        if row['Kyn'] == 'Alls':
            avg_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Karlar':
            avg_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Konur':
            avg_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']


avg_all = dict_sort.key_sort(avg_all)
avg_kk = dict_sort.key_sort(avg_kk)
avg_kvk = dict_sort.key_sort(avg_kvk)

x = list()
y = list()
for i in range(len(avg_all)):
    x.append(int(avg_all[i][0]))
    y.append(int(avg_all[i][1]))

xkk = list()
ykk = list()
for i in range(len(avg_kk)):
    xkk.append(int(avg_kk[i][0]))
    ykk.append(int(avg_kk[i][1]))

xkvk = list()
ykvk = list()
for i in range(len(avg_kvk)):
    xkvk.append(int(avg_kvk[i][0]))
    ykvk.append(int(avg_kvk[i][1]))

line_all = plt.plot(x, y)#, align = 'center')
line_kk = plt.plot(xkk, ykk)#,align = 'center')
line_kvk = plt.plot(xkvk, ykvk)#,align = 'center')
plt.title('Heildarlaun - Meðaltal í fullri vinnu milli ára í þús. kr.')
plt.legend( ('Alls', 'Karlar', 'Konur'), loc = 'upper left' )
#plt.xticks([year for year in x if year % 2 == 0])
#plt.xlim(1997, 2015)
plt.show()
        

print()
print()
data.print_keys()
