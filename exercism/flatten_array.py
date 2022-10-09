def flatten(iterable):
    item = []
    for x in iterable:
        if type(x) == list:
            item += flatten(x)
        elif x is not None:
            item.append(x)
    return item
