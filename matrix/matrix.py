class Matrix(object):
    def __init__(self, m_str):
        self.matriz=[]
        for fila in m_str.split("\n"):
            self.matriz.append([int(x) for x in fila.split(" ")])

    def row(self, i):
        return self.matriz[i-1]

    def column(self, i):
        return [fila[i-1] for fila in self.matriz]