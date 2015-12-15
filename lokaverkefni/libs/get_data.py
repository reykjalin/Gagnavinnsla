from execute_query import run_query
from libs.get_coords import get_coords
from SpinTest import plot2D

def get_conflicts(engine, year):
    Cdata = run_query(engine, 'distinct location', 'conflict', 'where year = {}'.format(year))
    Clats, Clons = get_coords(Cdata)

    Elats = run_query(engine, 'lat', 'eclipse', 'where year = {}'.format(year))
    Elons = run_query(engine, 'long', 'eclipse', 'where year = {}'.format(year))
    
    return plot2D(Elats,Elons,True,Clats,Clons,True)
    
def get_maxyear(engine):
    return run_query(engine, 'max(year)', 'conflict').fetchall()[0][0]

def get_minyear(engine):
    return run_query(engine, 'min(year)', 'conflict').fetchall()[0][0]
