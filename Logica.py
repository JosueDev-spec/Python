class Logica:
    def __init__(self):
        pass
    def calculadora(self, n1, operador, n2):
        resutado = 0
        if operador == 1:
            resutado = n1 + n2
        elif operador == 2:
            resutado = n1 - n2
        elif operador == 3:
            resutado = n1 * n2
        elif operador == 4:
            resutado = n1 / n2
        return resutado
