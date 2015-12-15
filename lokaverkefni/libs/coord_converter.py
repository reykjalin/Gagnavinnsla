def to_num(lats, lons):
    for i in range(len(lats)):
        if lats[i].endswith('N'):
            lats[i] = int(lats[i][:-1])
        else:
            lats[i] = int('-' + lats[i][:-1])
            
        if lons[i].endswith('E'):
            lons[i] = int(lons[i][:-1])
        else:
            lons[i] = int('-' + lons[i][:-1])
    return lats, lons

def to_str(lats, lons):
    for i in range(len(lats)):
        if str(lats[i]).startswith('-'):
            lats[i] = str(lats[i])[1:] + 'S'
        else:
            lats[i] = str(lats[i]) + 'N'

        if str(lons[i]).startswith('-'):
            lons[i] = str(lons[i])[1:] + 'W'
        else:
            lons[i] = str(lons[i]) + 'E'
