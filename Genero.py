from PyMySQL import DB

class Genero(object):
    idGenero = None
    Nombre_Genero = None

    def __init__(self,ng):
        self.Nombre_Genero = ng

    def InsertGen(self,ng):

        DB.run("insert into Genero values (null,'%s');" % (ng))

    def LeerGen(self):
        cursor = DB.run("select * from Genero;")
        lista = []
        for b in cursor:
            Gen = Genero( b['Nombre_Genero'])

            lista.append(Gen)

        return lista

    def BorrarGen(self):
        DB.run("delete from Genero where idGenero = %s;" % (self.idGenero))

    def ActualizarGen(self):
        DB.run("update Genero set Nombre_Genero = '%s'; " % (self.Nombre_Genero))
