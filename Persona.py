import Registro

class Persona (object):
    Nombre = None
    Apellido = None
    FechanNac = None

    def __init__(self, Nombre, Apellido, FechaNac):
        self.ListaRegistros = []
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaNac = FechaNac

    def agregarRegistro(self, Altura, Peso, FechaHoy):
        r = Registro(Altura, Peso, FechaHoy)
        self.ListaRegistros.append(r)