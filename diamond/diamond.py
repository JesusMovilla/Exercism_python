def rows(letter):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = letters.find(letter)
    res = []
    for i in range(length+1):
        if i == 0:
            res.append(' '*length + 'A' + ' '*length)
        else:
            res.append(' '*(length-i) + letters[i] + ' '*(i*2-1) + letters[i] +
                       ' '*(length-i))
    return res + res[0:-1][::-1]
