import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4]
y = x
ax = fig.add_subplot(111)
ax.plot(x,y, 'o', picker=5)

def onpick(event):
    mouseevent = event.mouseevent
    artist = event.artist
    ind = event.ind
    print(x[ind])

	

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()