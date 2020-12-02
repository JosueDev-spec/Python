class Interfaz:
    def __init__(self):
        pass

    def solicitar_numero(self):
        n1 = int(input("Digite un numero >"))
        return n1
    def solicitar_operador(self):
        operador =int(input("Digite un el operador : \n1-Suma (+)\n2-Resta(-)\n3-Multiplicacion(*)\n4-Division(/)\n > "))
        return  operador
    def mostar_resultado(self, resultado):
        print("R/ "+str(resultado))