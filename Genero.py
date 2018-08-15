from PyMySQL import DB

class Genero(object):
    idGenero = None
    Nombre_Genero = None

    def __init__(self,id,ng):
        self.idGenero = id
        self.Nombre_Genero = ng



    def InsertGen(ng):

        DB.run("insert into Genero values (NULL,'%s');" % (ng))

    @staticmethod
    def LeerGen(id):
        cursor = DB.run("select * from Genero join Album_has_Genero on Album_has_Genero.Genero_idGenero = Genero.idGenero where Album_idAlbum = '%s';" % (id))
        lista = []
        for b in cursor:
            Gen = Genero(b['idGenero'], b['Nombre_Genero'])

            lista.append(Gen)

        return lista

    def BorrarGen(self,id):
        DB.run("delete from Genero where idGenero = %s;" % (id))

    def ActualizarGen(self,ng,id):
        DB.run("update Genero set Nombre_Genero = '%s' where idGenero = '%s'; " % (ng,id))
