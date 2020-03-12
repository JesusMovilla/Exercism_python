def transpose(lines):
    lines = lines.split('\n')
    x = max([len(line) for line in lines])
    matrix = [[] for i in range(x)]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix[j].append(char)
        if i != 0:
            x = max([len(line) for line in lines[i:]])
        for j in range(len(line), x):
            matrix[j].append(' ')
    matrix = [''.join(row) for row in matrix]
    return '\n'.join(matrix)
