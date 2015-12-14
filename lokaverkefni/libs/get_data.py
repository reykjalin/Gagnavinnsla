from execute_query import run_query
from libs.get_coords import get_coords
from SpinTest import plot2D

def get_conflicts(engine, year):
    data = run_query(engine, 'distinct location', 'conflict', 'where year = {}'.format(year))
    lats, lons = get_coords(data)
    return plot2D(lats, lons)
    
def get_maxyear(engine):
    return run_query(engine, 'max(year)', 'conflict')

def get_minyear(engine):
    return run_query(engine, 'min(year)', 'conflict')
