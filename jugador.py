class jugador(object):
    Nombre = None
    FechaNac = None
    NumeroCamiseta = None
    Capitan = False

    def __init__(self,Nombre,FechaNac,NumeroCamiseta):
        self.Nombre = Nombre
        self.FechaNac = FechaNac
        self.NumeroCamiseta = NumeroCamiseta

    def setCapitan(self,Capitan):
        self.Capitan = Capitan

