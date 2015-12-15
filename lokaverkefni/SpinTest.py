# coding=utf-8
# Til að keyra þessa skrá þarf að installa:
# Basemap í gegnum pip
# Pillow í gegnum pip

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import PIL


def onpick(event):

    ind = event.ind
    artist = event.artist
    xdata = artist.get_xdata()
    ydata = artist.get_ydata()


    if ind[0] in range(len(xdata)):
        print('The coordinates are {}, {}'.format(xdata[ind[0]],ydata[ind[0]]))
    return ind[0]


# Takes the lattitutes, longitudes and countries as a lists and plots
def plotme(lats,lons):
    count = 0

    # Rotate the earth
    for l in range((2*count-180),180,2):
        fig = plt.figure(figsize=(10,10))
        map = Basemap(projection='ortho', lat_0 = 23.4 , lon_0 = l ,resolution = 'l')

        # Make the globe more realistic
        map.bluemarble()

        # compute the native map projection coordinates for countries.
        x,y = map(lons,lats)

        # plot solar eclipse positions
        map.plot(x,y,'rx', ms=6)

        plt.savefig("globeframes/frame{0}".format((str(count).rjust(3, "0"))), facecolor='k')
        count += 1
        plt.clf()
        plt.close(fig)


def plot2D(Elats,Elons,plotEclipse,Clats,Clons,plotConflict):

    # Making the plot fullscreen
    fig = plt.figure(figsize=(20,9))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])

    map = Basemap(projection='cyl',resolution='c')
    map.drawcoastlines()
    #map.fillcontinents(color='coral',lake_color='aqua')
    #map.drawmapboundary(fill_color='aqua')
    map.bluemarble()
    #draw the edge of the map projection region
    map.drawcountries()
    map.drawstates()

    if plotEclipse:
    # compute the native map projection coordinates for countries.
        x,y = map(Elons,Elats)

        # plot filled circles at the locations of the contry.
        map.plot(x,y,'kx', ms=10, picker=5,mew = 4)

    if plotConflict:

        x,y = map(Clons,Clats)
        map.plot(x,y,'rx', ms=10, picker=5,mew = 4)

    # for i in range(len(countries)):
    #     text = plt.text(lons[i], lats[i], countries[i],fontsize=12,fontweight='bold',color='k')
    #     text.set_visible(False)

    # fig.canvas.mpl_connect('pick_event', onpick)
    return fig
    #plt.show()

def plotmap():
    fig = plt.figure(figsize=(20,9))
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98])

    map = Basemap(projection='cyl',resolution='c')
    map.drawcoastlines()
    #map.fillcontinents(color='coral',lake_color='aqua')
    #map.drawmapboundary(fill_color='aqua')
    map.bluemarble()
    #draw the edge of the map projection region
    map.drawcountries()
    map.drawstates()

    return fig

