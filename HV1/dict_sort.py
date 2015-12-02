def sort(d):
    items = [(v, k) for k, v in d.items()]
    items.sort()
    items = [(k, v) for v, k in items]
    return items
