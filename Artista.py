from PyMySQL import DB

class Artista(object):
    idArtista = None
    Nombre = None
    Conciertos = None

    def __init__(self,id,n,c):
        self.idArtista = id
        self.Nombre = n
        self.Conciertos= c

    def InsertArt(self,n,c):

        DB.run("insert into Artista values (null,'%s','%s');" % (n,c))

    def LeerArt(self):
        cursor = DB.run("select * from Artista;")
        lista = []
        for b in cursor:

            Art = Artista(b['idArtista'],b['Nombre'], b['Conciertos'])

            lista.append(Art)

        return lista


    def BorrarArt(self,id):
        DB.run("delete from Artista where idArtista = %s;" % (id))

    def ActualizarArt(self,n,c,id):
        DB.run("update Artista set Nombre = '%s' , Conciertos = '%s' where idArtista = %s; " % (n,c,id))
