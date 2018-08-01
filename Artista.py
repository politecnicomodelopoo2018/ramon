from PyMySQL import DB

class Artista(object):
    idArtista = None
    Nombre = None
    Conciertos = None

    def InsertArt(self, idArtista, Nombre, Conciertos):

        DB.run("insert into Artista values (null,'" + self.Nombre + "','" + self.Conciertos + "')")



    def LeerArt(self):
        a = DB.connect("select * from Artista")
        lista = []
        for b in a:
            Art = Artista(b['idArtista'], b['Nombre'], b['Conciertos'])

        lista.append[Art]

        return lista

    def BorrarArt(self):
        a = DB.connect("delete from Artista where idArtista = %s" % (self.idArtista))

    def ActualizarArt(self):
        a = DB.connect("update Artista set Nombre = '%s' , Conciertos = '%s' ; " % (self.Nombre,self.Conciertos))
