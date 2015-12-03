import read_csv as data
import dict_sort
import matplotlib.pyplot as plt
import avg_sal as avg

#avg.prepare_data()

plt.figure()
avg.plot_avg()
plt.grid()

plt.twinx()
avg.plot_ar()


plt.show()
