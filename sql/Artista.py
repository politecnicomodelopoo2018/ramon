from MySQL import DB

class Artista(object):
    idArtista = None
    Nombre = None
    Apellido = None
    Conciertos = None

    def SetInsert(self, idArtista, Nombre, Apellido, Conciertos):

        DB.run("insert into Artista values (null,'" + self.Nombre + "','" + self.Apellido + "')")
