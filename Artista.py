from PyMySQL import DB

class Artista(object):
    idArtista = None
    Nombre = None
    Conciertos = None

    def __init__(self,n,c):
        self.Nombre = n
        self.Conciertos= c

    def InsertArt(self):

        DB.run("insert into Artista values (null,'%s','%s');" % (self.Nombre, self.Conciertos))

    def LeerArt(self):
        cursor = DB.run("select * from Artista;")
        lista = []
        for b in cursor:
            Art = Artista(b['Nombre'], b['Conciertos'])

        lista.append(Art)

        return lista


    def BorrarArt(self):
        DB.run("delete from Artista where idArtista = %s;" % (self.idArtista))

    def ActualizarArt(self):
        DB.run("update Artista set Nombre = '%s' , Conciertos = '%s'; " % (self.Nombre,self.Conciertos))
