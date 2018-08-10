from PyMySQL import DB

class Genero(object):
    idGenero = None
    Nombre_Genero = None
    idGenero_Album = None

    def __init__(self,id,ng,id_alb):
        self.idGenero = id
        self.Nombre_Genero = ng
        self.idGenero_Album = id_alb

    def InsertGen(self,ng,id_alb):

        DB.run("insert into Genero values (null,'%s','%s');" % (ng,id_alb))

    def LeerGen(self):
        cursor = DB.run("select * from Genero;")
        lista = []
        for b in cursor:
            Gen = Genero(b['idGenero'], b['Nombre_Genero'])

            lista.append(Gen)

        return lista

    def BorrarGen(self,id):
        DB.run("delete from Genero where idGenero = %s;" % (id))

    def ActualizarGen(self):
        DB.run("update Genero set Nombre_Genero = '%s'; " % (self.Nombre_Genero))
