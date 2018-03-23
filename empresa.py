from Empleado import Empleado


class Empresa(object):
    nombre = None

    def __init__(self):
        self.listaEmp = []

    def AgregarEmpleado(self, nombre, apellido, tel, fecha):
        empleado = Empleado()

        empleado.setNombre(nombre)
        empleado.setApellido(apellido)
        empleado.setTelefono(tel)
        empleado.setNac(fecha)
        self.listaEmp.append(empleado)

    def setDiasAasisitir(self,a,nombre):

        for item in self.listaEmp:
        if item.nombre == nombre:
            item.listaAsis.append(a)

    def Fichar(self, nombre, fecha):
        for item in self.listaEmp:
            if item.nombre  == nombre:
               item.listaAsis.append(fecha)

    def VerPromMes (self,nombre):
        for item in self.listaEmp:
            if item.nombre  == nombre:
               item.promMes()