import read_csv as data
import dict_sort
import matplotlib.pyplot as plt

AKKHeildFullMedal = dict()

for row in data.vinna:
    if row['Starfsstétt'] == 'Alls' and row['Kyn'] == 'Alls':
        AKKHeildFullMedal[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']

AKKHeildFullMedal = dict_sort.sort(AKKHeildFullMedal)

x = list()
y = list()
for key in list(AKKHeildFullMedal.keys()):
    x.append(int(key))
    y.append(int(AKKHeildFullMedal[key]))

plt.bar(x, y, align = 'center')
plt.title('Heildarlaun - Meðaltal í fullri vinnu milli ára í þús. kr.')
plt.xticks([year for year in x if year % 2 == 0])
plt.xlim(1997, 2015)
plt.show()
        

print()
print()
data.print_keys()
