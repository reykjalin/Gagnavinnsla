def tuple2_tofloat(l):
    newl = list()
    for x,y in l:
        try:
            newl.append((float(x),float(y)))
        except:
            pass
    return newl