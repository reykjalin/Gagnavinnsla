import matplotlib.pyplot as plt

from spurningarvladimir import aldurshop_mentun
from read_csv import print_keys
from avg_sal import average_sal
from spurningarhaukur import innanh_vs_utanh
from q1_q3_munur import average_and_std_laun

# start skjal
print_keys()

# vladimir
aldurshop_mentun()

# Krilli + Jón
average_sal(5)

# Haukur
innanh_vs_utanh()
average_and_std_laun()

# Róbert

plt.show()