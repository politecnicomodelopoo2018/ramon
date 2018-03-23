import datetime

class Alumno (object):
    nombre = None
    apellido = None
    fechaNac = None
    def __init__(self):
        self.listaNotas=[]



    def setNombre (self,nombre):
        self.nombre = nombre
    def setApellido (self,apellido):
        self.apellido = apellido
    def setFechaNac (self,fecha):
        self.fechaNac = fecha
    def AgregarNota (self,nota):
        if nota > 10:
            return False
        if nota < 1:
            return False
        self.listaNotas.append(nota)
        return True
    def mayorNota (self):
        return max(self.listaNotas)

    def Edad (self):
        fecha = datetime.date.today()
        dif = fecha - self.fechaNac
        self.dias = dif.days
        return self.dias/365.25  #Sacar la edad