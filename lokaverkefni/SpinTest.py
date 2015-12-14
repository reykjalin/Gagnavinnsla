# Til að keyra þessa skrá þarf að installa:
# Basemap í gegnum pip
# Pillow í gegnum pip

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import PIL

# Takes the lattitutes, longitudes and countries as a lists and plots
def plotme(lats,lons):
    count = 0

    # Rotate the earth
    for l in range((2*count-180),180,2):
        fig = plt.figure(figsize=(10,10))
        map = Basemap(projection='ortho', lat_0 = 23.4 , lon_0 = l ,resolution = 'l')

        # Make the globe more realistic
        map.bluemarble()

        # compute the native map projection coordinates for contries.
        x,y = map(lons,lats)

        # plot solar eclipse positions
        map.plot(x,y,'rx', ms=6)

        plt.savefig("globeframes/frame{0}".format((str(count).rjust(3, "0"))), facecolor='k')
        count += 1
        plt.clf()
        plt.close(fig)

def plot2D(lats,lons,contries,year):

	# Making the plot fullscreen
	fig = plt.figure(figsize=(20,9))
	ax = fig.add_subplot(111)

	map = Basemap(projection='cyl',resolution='c')
	map.drawcoastlines()
	map.fillcontinents(color='coral',lake_color='aqua')
	map.drawmapboundary(fill_color='aqua')

	#draw the edge of the map projection region
	map.drawcountries()
	map.drawstates()

	# compute the native map projection coordinates for contries.
	x,y = map(lons,lats)

	# plot filled circles at the locations of the contry.
	map.plot(x,y,'rx', ms=5, picker=5)

	for i in range(len(contries)):
		text = plt.text(lons[i], lats[i], contries[i],fontsize=12,fontweight='bold',color='k')
		text.set_visible(False)

	def onpick(event,countries):
	    ind = event.ind

	    #print('The coordinates are {}, {}'.format(lats[ind],lons[ind]))

	    for i in range(len(countries)):
	    	if ind == i:
	    		print(countries[i])



	fig.canvas.mpl_connect('pick_event', onpick(countries))

	plt.show()
	#plt.savefig("mapframes/year{0}".format((str(year)), facecolor='k')
	#plt.clf()






