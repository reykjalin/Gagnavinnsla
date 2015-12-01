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
for pair in AKKHeildFullMedal:
    print(pair[0], pair[1], sep = '\t')
    x.append(int(pair[0]))
    y.append(int(pair[1]))

plt.bar(x, y)
plt.title('Heildarlaun - Meðaltal í fullri vinnu milli ára í þús. kr.')
plt.show()
        

print()
print()
data.print_keys()
