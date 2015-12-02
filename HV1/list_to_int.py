def toint(l):
    newl = list()
    for i in l:
        try:
            newl.append(int(i))
        except:
            pass
    return newl

def tuple2_toint(l):
    newl = list()
    for x,y in l:
        try:
            newl.append((int(x),int(y)))
        except:
            pass
    return newl
