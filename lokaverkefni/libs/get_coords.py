from pygeocoder import Geocoder # pip install pygeocoder
from libs.execute_query import run_query
from libs.coord_converter import to_num, to_str

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

def get_locs_db(engine, tablename, wh_cond, orderby = ''):
    return run_query(engine, 'distinct location', tablename, wh_cond, '', orderby).fetchall()

def get_coords_db(engine, tablename, wh_cond, orderby = ''):
    coords = run_query(engine, 'distinct lat, long', tablename, wh_cond, '', orderby).fetchall()
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
        loc = get_locs_db(engine, table, "where to_char(lat, '999D9') = to_char({}, '999D9') and to_char(long, '999D9') = to_char({}, '999D9')".format(lats[i], lons[i]))
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

def get_export_typeprice(engine, year):
    typeprice = run_query(engine, 'type, price', 'export', 'where year = {}'.format(year)).fetchall()
    return typeprice

def get_confinfo_data(engine, lat, lon, year):
    loc = get_loc_from_coords_db(engine, [lat,], [lon,], 'conflictlc')[0][0][0]
    return run_query(engine, 'location, sidea, sideb, territoryname, startdate, ependdate', 'conflict', "where year = {} and location like '%%{}%%'".format(year, loc), '', 'order by location, startdate, sidea, sideb, territoryname').fetchall()

def get_eclipse_data(engine, lat, lon, year):
    lat, lon = to_str([lat,], [lon,])
    return run_query(engine, 'calendardate, central_dur, ecl_type, sun_alt, path_width', 'eclipse', "where lat = '{}' and long = '{}' and calendardate_year = {}".format(lat[0], lon[0], year)).fetchall()


def get_all_conflicts(engine):
    data = run_query(engine, 'lat, long', 'conflictlc').fetchall()
    print(data)

def get_all_eclipses(engine):
    data = run_query(engine, 'lat, long', 'eclipselc').fetchall()
    print(data)
