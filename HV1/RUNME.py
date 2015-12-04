import matplotlib.pyplot as plt

from spurningarvladimir import aldurshop_mentun
from read_csv import print_keys
import avg_sal as avg
from spurningarhaukur import innanh_vs_utanh
from q1_q3_munur import average_and_std_laun

# start skjal
print_keys()

# vladimir
aldurshop_mentun()

# Krilli + Jón
plt.figure(5)
avg.plot_avg()
plt.ylabel('Heildarlaun í þús. kr.')
plt.xlabel('Ár')
plt.legend(['Laun - Alls', 'Laun - Karlar', 'Laun - Konur'], loc='upper left')

plt.twinx()

avg.plot_ar()
plt.ylabel('Fjöldi háskólamenntaðra einstaklinga')
plt.legend(['Menntun - Alls', 'Menntun - Karlar', 'Menntun - Konur'], loc='center left')
plt.title('Heildarlaun og háskólamenntun')


plt.figure(9)
avg.plot_skrifst()
plt.ylabel('Heildarlaun í þús. kr.')
plt.xlabel('Ár')
plt.legend(['Alls', 'Karlar', 'Konur'], loc='upper left')
plt.title('Heildarlaun skrifstofufólks')
plt.grid()

plt.figure(10)
plt.subplot(2,1,1)
avg.plot_serfr()
plt.legend(['Laun - Alls', 'Laun - Karlar', 'Laun - Konur'], loc='upper left')
plt.title('Heildarlaun Sérfræðinga')
plt.grid(axis='y')

plt.subplot(2,1,2)
avg.plot_stjorn()
plt.legend(['Laun - Alls', 'Laun - Karlar', 'Laun - Konur'], loc='upper left')
plt.title('Heildarlaun Stjórnenda')
plt.grid(axis='y')

# Haukur
innanh_vs_utanh()
average_and_std_laun()

# Róbert

plt.show()
