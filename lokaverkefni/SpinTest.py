# Til að keyra þessa skrá þarf að installa:
# Basemap í gegnum pip
# Pillow í gegnum pip

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import PIL
#from datetime import datetime


# Takes the lattitutes, longitudes and countries as a lists and plots
def plotme(lats,lons,ymds):
	count = 159

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



