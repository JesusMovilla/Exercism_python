def slices(series, length):
    if length > 0 and length <= len(series):
        return [series[x:x+length] for x in range(0, len(series) - length + 1)]
    else:
        raise ValueError(ValueError)
