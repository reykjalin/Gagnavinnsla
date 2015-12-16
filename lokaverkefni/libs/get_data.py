# coding=utf-8
from libs.execute_query import run_query
from libs.get_coords import get_locs_db, get_coords_from_loc_db, get_eclipse_coords, get_export_typeprice, get_confinfo_data, get_eclipse_data
from libs.SpinTest import plot2D, plotme

def get_conflicts(engine, year,Eplot,Cplot,TwoD):
    Cdata = get_locs_db(engine, 'conflict', 'where year = {}'.format(year))
    Clats, Clons = get_coords_from_loc_db(engine, Cdata, 'conflictlc')
    Elats, Elons = get_eclipse_coords(engine, year)
    return plot2D(Elats,Elons,Eplot,Clats,Clons,Cplot,TwoD)

def makethevideo(engine,year,Eplot,Cplot):
    Cdata = get_locs_db(engine, 'conflict', 'where year = {}'.format(year))
    Clats, Clons = get_coords_from_loc_db(engine, Cdata, 'conflictlc')
    Elats, Elons = get_eclipse_coords(engine, year)
    plotme(Elats,Elons,Eplot,Clats,Clons,Cplot)

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

def get_eclipseinfo(engine, lat, lon, year):
    info = ''
    data = get_eclipse_data(engine, lat, lon, year)
    for d in data:
        d = dict(d.items())
        for i in d.keys():
            if d[i] is None:
                d[i] = '-'

        if d['ecl_type'].startswith('P'):
            etype = 'Partial'
        elif d['ecl_type'].startswith('A'):
            etype = 'Annular'
        elif d['ecl_type'].startswith('T'):
            etype = 'Total'
        elif d['ecl_type'].startswith('H'):
            etype = 'Hybrid'
        else:
            etype = '-'
        info += 'Date: ' + str(d['calendardate']) + '\n' +\
                'Duration: ' + d['central_dur'] + '\n' +\
                'Type: ' + etype + '\n' +\
                'Sun altitude: ' + str(d['sun_alt']) + '°' + '\n' +\
                'Path width: ' + d['path_width'] + 'km' + '\n\n'
    return info
