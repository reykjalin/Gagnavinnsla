from pygeocoder import Geocoder # pip install pygeocoder
from libs.execute_query import run_query
from libs.coord_converter import to_num

def get_coords_geocoder(locs):
    retlat = []
    retlon = []
    for loc in locs:
        g = Geocoder.geocode(loc)[0].coordinates
        retlat.append(g[0])
        retlon.append(g[1])
    return retlat, retlon

def get_loc_geocoder(lats, longs):
    retloc = []
    for i in range(len(lats)):
        try:
            g = Geocoder.reverse_geocode(lats[i], longs[i])
            retloc.append(g.country)
        except:
            retloc.append('N/A')
    return retloc

def get_locs_db(engine, tablename, wh_cond):
    return run_query(engine, 'distinct location', tablename, wh_cond)

def get_coords_db(engine, tablename, wh_cond):
    coords = run_query(engine, 'distinct lat, long', tablename, wh_cond).fetchall()
    return coords[0][0], coords[0][1]

def get_coords_from_loc_db(engine, locs, table):
    retlat = []
    retlon = []
    for loc in locs:
        wh = loc[0].split(',')
        for l in wh:
            lat, lon = get_coords_db(engine, table, "where location = '" + l.strip() + "'")
            retlat.append(lat)
            retlon.append(lon)
    return retlat, retlon

def get_loc_from_coords_db(engine, lats, lons, table):
    locs = []
    for i in range(len(lats)):
        loc = get_locs_db(engine, table, "where lat = " + lats[i] + " and long = " + lons[i])
        locs.append(loc)
    return locs

def get_eclipse_coords(engine, year):
    coords = run_query(engine, 'distinct lat, long', 'eclipse', 'where calendardate_year = {}'.format(year)).fetchall()
    lats = []
    lons = []
    for coord in coords:
        lats.append(coord[0])
        lons.append(coord[1])
    lats, lons = to_num(lats, lons)
    return lats, lons
