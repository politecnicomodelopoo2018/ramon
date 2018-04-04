from Registro import Registro
import Persona
import datetime

Año = None
p= Persona()
a = datetime.date (2001, 6, 1)
b = datetime.date.today
p.setNombre("Ramon")
p.setApellido("Labioconcha")
p.setFechaNac(a)
FechaHoy = datetime.date.today()