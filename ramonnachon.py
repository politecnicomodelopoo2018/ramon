from jugador import jugador

import calendar

class equipo(object):
    NombreEquipo = None
    Barrio = None
    Turno = None
    ListaJugadores = []
    ListaDias =[True, True, True, True, True, True, False]

    def __init__(self,NombreEquipo,Barrio,Turno):
        self.NombreEquipo = NombreEquipo
        self.Barrio = Barrio
        self.Turno = Turno

    def agregarjugador(self,Nombre,FechanNac,NumeroCamiseta):
        j = jugador(Nombre,FechanNac,NumeroCamiseta)
        self.ListaJugadores.append(j)

    def setCap(self,Nombre,Capitan):
        for item in self.ListaJugadores:
            if item.Nombre == Nombre:
                item.setCapitan(Capitan)

    def HorariosEquipos (self, dia):
        DiasDisponibles = calendar.weekday()
        



