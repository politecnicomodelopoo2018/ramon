from PyMySQL import DB

class Cancion(object):
    idCancion = None
    Nombre_Cancion = None
    idCancion_Artista = None
    idCancion_Album = None

    def __init__(self,id,nc,id_art,id_al):
        self.idCancion = id
        self.Nombre_Cancion = nc
        self.idCancion_Artista = id_art
        self.idCancion_Album = id_al

    def InsertCan(self,nc,id_art,id_al):

        DB.run("insert into Cancion values (null,'%s','%s','%s');" % (nc,id_art,id_al))

    def LeerCan(self,id_art,id_al):
        cursor = DB.run("select * from Cancion where Artista_idArtista = '%s' and Album_idAlbum = '%s';" % (id_art,id_al))
        lista = []
        for b in cursor:
            Can = Cancion(b['idCancion'],b['Nombre_Cancion'],b['Artista_idArtista'],b['Album_idAlbum'])
            lista.append(Can)
        return lista

    def BorrarCan(self,id):
        DB.run("delete from Cancion where idCancion = '%s';" % (id))

    def ActualizarCan(self,nc,id):
        DB.run("update Cancion set Nombre_Cancion = '%s' where idCancion = '%s'; " % (nc,id))
