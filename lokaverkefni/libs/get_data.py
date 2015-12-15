from libs.execute_query import run_query
from libs.get_coords import get_locs_db, get_coords_from_loc_db, get_eclipse_coords, get_export_typeprice, get_confinfo_data
from libs.SpinTest import plot2D, plotme

def get_conflicts(engine, year):
    Cdata = get_locs_db(engine, 'conflict', 'where year = {}'.format(year))
    Clats, Clons = get_coords_from_loc_db(engine, Cdata, 'conflictlc')
    Elats, Elons = get_eclipse_coords(engine, year)
    return plot2D(Elats,Elons,True,Clats,Clons,True,True)

def get_conflicts3D(engine, year):
    Cdata = get_locs_db(engine, 'conflict', 'where year = {}'.format(year))
    Clats, Clons = get_coords_from_loc_db(engine, Cdata, 'conflictlc')
    Elats, Elons = get_eclipse_coords(engine, year)
    plot2D(Elats,Elons,True,Clats,Clons,True, False)
    
    
def get_maxyear(engine):
    return run_query(engine, 'max(year)', 'conflict').fetchall()[0][0]

def get_minyear(engine):
    return run_query(engine, 'min(year)', 'conflict').fetchall()[0][0]

def get_conflist(engine, year):
    loctxt = ''
    locs = get_locs_db(engine, 'conflict', 'where year = {}'.format(year), 'order by location')
    for loc in locs:
        loctxt += loc[0] + '\n\n'
    return loctxt

def get_exportlist(engine, year):
    exptxt = ''
    exp = get_export_typeprice(engine, year)
    for typeprice in exp:
        exptxt += typeprice[0] + ': ' + str(int(typeprice[1])) + '\n\n'
    return exptxt

def get_confinfo(engine, lat, lon, year):
    info = ''
    data = get_confinfo_data(engine, lat, lon, year)
    print('data: ', data)
    for d in data:
        d = dict(d.items())
        for i in d.keys():
            if d[i] is None:
                d[i] = '-'
        info += 'Location: ' + d['location'] + '\n' + \
                'Side A: ' + d['sidea'] + '\n' + \
                'Side B: ' + d['sideb'] + '\n' + \
                'Territory: ' + d['territoryname'] + '\n' + \
                'Start: ' + d['startdate'] + '\n' +\
                'End: ' + d['ependdate'] + '\n\n'
    return info
