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

    def LeerCan(self):
        cursor = DB.run("select * from Cancion;")
        lista = []
        for b in cursor:
            Can = Cancion(b['idCancion'],b['Nombre_Cancion'],b['Artista_idArtista'],b['Album_idAlbum'])
            lista.append(Can)
        return lista

    def BorrarCan(self,id):
        DB.run("delete from Cancion where idCancion = %s;" % (id))

    def ActualizarCan(self):
        DB.run("update Cancion set Nombre_Cancion = '%s'; " % (self.Nombre_Cancion))
