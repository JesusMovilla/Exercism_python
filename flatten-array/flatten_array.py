def flatten(iterable):
    lista = list()
    for item in iterable:
        if isinstance(item, (list, tuple)):
            lista += flatten(item)
        elif item is not None:
            lista.append(item)
    return lista
