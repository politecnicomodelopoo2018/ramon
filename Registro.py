class Registro (object):
    Altura = None
    Peso = None
    Fecha = None

    def agregarRegistro(self, Altura, Peso, Fecha):
        self.Altura = Altura
        self.Peso = Peso
        self.Fecha = Fecha


    def Promedio (self, ListaRegistros, Año):
        for item in self.ListaRegistro:
            if item.Fecha.year == Año:
                return float(sum(ListaRegistros.Altura)) / max(len(ListaRegistros.Altura), 1)
                return float(sum(ListaRegistros.Peso)) / max(len(ListaRegistros.Peso), 1)

º