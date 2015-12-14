from pygeocoder import Geocoder # pip install pygeocoder

def get_coords(locs):
    retlat = []
    retlon = []
    for loc in locs:
        g = Geocoder.geocode(loc)[0].coordinates
        retlat.append(g[0])
        retlon.append(g[1])
    return retlat, retlon
