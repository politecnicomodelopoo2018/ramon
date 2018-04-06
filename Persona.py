import Registro

class Persona (object):
    Nombre = None
    Apellido = None
    FechaNac = None

    def __init__(self, Nombre, Apellido, FechaNac):
        self.ListaRegistros = []
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaNac = FechaNac

    def agregarMedia(self, altura, peso, fecha):
       unaMedida= Medida ()
       unaMedida.peso = peso
       unaMedida.altura = altura
       unaMedia.fecha = fecha
       self.listaMedidas.append (unaMedida)

    def promedioAlt (self, año) :
        s = 0
        c = 0

        for item in self.listaMedidas :
            if item.fecha.year == año:
                s + = item.año/7
                c + = 1

        return s/c