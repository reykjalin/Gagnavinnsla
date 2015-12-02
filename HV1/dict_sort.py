def value_sort(d):
    items = [(v, k) for k, v in d.items()]
    items.sort()
    items = [(k, v) for v, k in items]
    return items

def key_sort(d):
    items = [(k,v) for k, v in d.items()]
    items.sort()
    return items
