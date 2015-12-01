def sort(d):
    items = [(v, k) for k, v in d.items()]
    items.sort()
    items = [(k, v) for v, k in items]
    sorted_dict = dict()
    for (k,v) in items:
        sorted_dict[k] = v
    return sorted_dict
