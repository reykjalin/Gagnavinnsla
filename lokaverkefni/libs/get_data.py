from libs.execute_query import run_query
from libs.get_coords import get_locs_db, get_coords_from_loc_db, get_eclipse_coords
from libs.SpinTest import plot2D

def get_conflicts(engine, year):
    Cdata = get_locs_db(engine, 'conflict', 'where year = {}'.format(year))
    Clats, Clons = get_coords_from_loc_db(engine, Cdata, 'conflictlc')
    Elats, Elons = get_eclipse_coords(engine, year)
    return plot2D(Elats,Elons,True,Clats,Clons,True)
    
    
def get_maxyear(engine):
    return run_query(engine, 'max(year)', 'conflict').fetchall()[0][0]

def get_minyear(engine):
    return run_query(engine, 'min(year)', 'conflict').fetchall()[0][0]
