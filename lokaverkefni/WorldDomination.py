# coding=utf-8
# Til að keyra þessa skrá þarf að installa:
# Basemap í gegnum pip
# Pillow í gegnum pip

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import PIL
# from datetime import datetime
# set up orthographic map projection with
# perspective of satellite looking down at 66N, 30W.
# use low resolution coastlines.
# don't plot features that are smaller than 1000 square km.


# Takes the lattitutes, longitudes and countries as a ints and plots
def plotme(lats,lons,contries,ymds):
	# Making the plot fullscreen
	fig = plt.figure(figsize=(20,9))
	fig.patch.set_facecolor('k')

	map = Basemap(projection='ortho', lat_0 = -90 , lon_0 = 0 ,resolution = 'l')

	# Make the globe more realistic
	map.bluemarble()

	#draw the edge of the map projection region (the projection limb)
	#map.drawmapboundary()
	#map.drawcountries()
	#map.drawstates()

	# draw lat/lon grid lines every 30 degrees.
	#map.drawmeridians(np.arange(0, 360, 30))
	#map.drawparallels(np.arange(-90, 90, 30))


	#CS = map.nightshade(ymds)

	# compute the native map projection coordinates for contries.
	x,y = map(lons,lats)

	# plot circle.
	map.plot(x,y,'rx', ms=10, mew=5)



	plt.show()