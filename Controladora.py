from Interfaz import Interfaz
from  Logica import Logica
class Controladora:
    def __init__(self):
        pass
    def InciarAcciones(self):
        miInterfaz = Interfaz()
        log = Logica()
        while True:
         n1 = miInterfaz.solicitar_numero()
         n2 = miInterfaz.solicitar_numero()
         operador = miInterfaz.solicitar_operador()
         resultado = log.calculadora(n1, operador, n2)
         miInterfaz.mostar_resultado(resultado)
