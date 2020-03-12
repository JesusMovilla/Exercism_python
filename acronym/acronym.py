def abbreviate(words):
    x = ""
    for i in words.replace('-', ' ').replace('_', ' ').split():
        x += i[0].upper()
    return x
