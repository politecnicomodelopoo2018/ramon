from PersonaEJ2 import ListaPlatos []
import Comida

class Familia (object):
    ListaFamilia = []

    def __init__ (self)
        self.ListaFamilia = []

    def agregarIntegrantesFlia(self, unaPersona):
        self.listaIntegrantesFlia.appened(unaPersona)

    def PromedioCalorias(self):
        s = 0;

        for item in self.ListaFamilia:
            s += item.sumaCalorias

        return s/len(self.ListaFamilia)

    def PersonaQueMasCaloriasConsumo(self):

        n = 0
        p = 0

        for item in self.ListaFamilia:
            if item.sumaCalorias
