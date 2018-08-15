from PyMySQL import DB

class Album(object):
    idAlbum = None
    Nombre_Album = None
    Fecha_Lanzamiento = None

    def __init__(self,id,n,f):
        self.idAlbum = id
        self.Nombre_Album = n
        self.Fecha_Lanzamiento = f

    def InsertAl(self,n,f):

        DB.run("insert into Album values (null,'%s','%s');" % (n, f))

    def LeerAl(self):
        cursor = DB.run("select * from Album;")
        lista = []
        for b in cursor:
            Al = Album(b['idAlbum'],b['Nombre_Album'], b['Fecha_Lanzamiento'])

            lista.append(Al)

        return lista

    def BorrarAl(self,id):
        DB.run("delete from Album where idAlbum = '%s';" % (id))

    def ActualizarAl(self,n,f,id):
        DB.run("update Album set Nombre_Album = '%s' , Fecha_Lanzamiento = '%s' where idAlbum = '%s'; " % (n,f,id))
