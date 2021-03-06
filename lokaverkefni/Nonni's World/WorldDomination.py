# Til að keyra þessa skrá þarf að installa:
# Basemap í gegnum pip
# Pillow í gegnum pip

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import PIL
from datetime import datetime

# set up orthographic map projection with
# perspective of satellite looking down at 66N, 30W.
# use low resolution coastlines.
# don't plot features that are smaller than 1000 square km.

# Making the plot fullscreen
plt.figure(figsize=(20,9))

map = Basemap(projection='ortho', lat_0 = 45, lon_0 = -30,resolution = 'l', area_thresh = 1000.)

# Make the globe more realistic
map.bluemarble()

#draw the edge of the map projection region (the projection limb)
map.drawmapboundary()
map.drawcountries()
map.drawstates()

# draw lat/lon grid lines every 30 degrees.
#map.drawmeridians(np.arange(0, 360, 30))
#map.drawparallels(np.arange(-90, 90, 30))


# lat/lon coordinates of five contries.
lats = [64]
lons = [-20]
contries = ['Iceland']

#date = datetime.utcnow()
#CS = map.nightshade(date)


# compute the native map projection coordinates for contries.
x,y = map(lons,lats)

# plot filled circles at the locations of the contries.
map.plot(x,y,'ko', alpha=.7, ms=20)

# plot the names of those five contries.
for name,xpt,ypt in zip(contries,x,y):
    plt.text(xpt+90000,ypt+90000,name)



plt.show()