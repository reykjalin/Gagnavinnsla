import matplotlib.pyplot as plt

def plot_line(x, y, title, legend, leg_loc = 'upper right'):
    plt.plot(x, y)
    plt.title(title)
    plt.legend(legend, leg_loc)

