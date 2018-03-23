import datetime
import calendar
class Empleado(object):
    nombre = None
    apellido = None
    telefono = None
    fechaNac = None



    def __init__(self):
        self.listaDiasAsistir = [True,True,True,True,True,False,False]
        self.listaAsis = []
        self.dias = 0


    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setTelefono(self,tel):
        self.telefono = tel

    def setNac(self,fecha):
        self.fechaNac = fecha

    def setAsistencia(self,fecha):
        self.listaAsis.append(fecha)

    def promMes(self, año ,mes):
        a=calendar.monthrange(año, mes)
        for i in range(a):
            fecha=datetime.date(año,mes,i)
            diasem=fecha.weekday()
            if self.listaAsis[diasem] == True:
                for y in self.listaAsis:
                    if self.listaAsis[y]== fecha:
                        self.dias+=1
                        return (self.dias*100)/a
