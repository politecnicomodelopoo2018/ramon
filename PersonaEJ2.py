from Comida import Plato

class Personas (object):
    Nombre = None
    FechaNac = None

    def __init__ (self):
        self.ListaPlatos = []


    def agregarPlato(self, unPlato):

        self.ListaPlatos.append(unPlato)

    def SumaCalorias (self):

        s= 0

        for item in self.ListaPlatos:

            s += item.calorias

        return s