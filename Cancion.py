from PyMySQL import DB

class Cancion(object):
    idCancion = None
    Nombre_Cancion = None

    def __init__(self,nc):
        self.Nombre_Cancion = nc

    def TriggerCan (self):
        DB.run("drop trigger if exists BorrarCancion;"
               "delimiter $$"
               "create trigger BorrarCancion before delete on Cancion for each row"
               "begin"
               "delete from Artista;"
               "end $$"
               "delimiter;")

    def InsertCan(self):

        DB.run("insert into Cancion values (null,'%s');" % (self.Nombre_Cancion))

    def LeerCan(self):
        cursor = DB.run("select * from Cancion;")
        lista = []
        for b in cursor:
            Can = Cancion(b['idCancion'], b['Nombre_Cancion'])

        lista.append[Can]

        return lista

    def BorrarCan(self):
        DB.run("delete from Cancion where idCancion = %s;" % (self.idCancion))

    def ActualizarCan(self):
        DB.run("update Cancion set Nombre_Cancion = '%s'; " % (self.Nombre_Cancion))
