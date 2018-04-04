

class Registro (object):
    Altura = None
    Peso = None
    FechaHoy = None

    def agregarRegistro(self, Altura, Peso, FechaHoy):
        self.Altura = Altura
        self.Peso = Peso
        self.FechaHoy = FechaHoy


    def Promedio (self, ListaRegistros, Año):
        for item in self.ListaRegistro:
            if item.FechaHoy.year == Año:
                return float(sum(ListaRegistros.Altura)) / max(len(ListaRegistros.Altura), 1)
                return float(sum(ListaRegistros.Peso)) / max(len(ListaRegistros.Peso), 1)

