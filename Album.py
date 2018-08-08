from PyMySQL import DB

class Album(object):
    idAlbum = None
    Nombre_Album = None
    Fecha_Lanzamiento = None

    def __init__(self,n,f):
        self.Nombre_Album = n
        self.Fecha_Lanzamiento = f

    def TriggerAl (self):
        DB.run("drop trigger if exists BorrarAlbum;"
               "delimiter $$"
               "create trigger BorrarAlbum before delete on Album for each row"
               "begin"
               "delete from Genero;"
               "delete from Cancion;"
               "end $$"
               "delimiter;")

    def InsertAl(self,n,f):

        DB.run("insert into Album values (null,'%s','%s');" % (n, f))

    def LeerAl(self):
        cursor = DB.run("select * from Album;")
        lista = []
        for b in cursor:
            Al = Album(b['Nombre_Album'], b['Fecha_Lanzamiento'])

            lista.append(Al)

        return lista

    def BorrarAl(self):
        DB.run("delete from Album where idAlbum = %s;" % (self.idAlbum))

    def ActualizarAl(self):
        DB.run("update Album set Nombre_Album = '%s' , Fecha_Lanzamiento = '%s'; " % (self.Nombre_Album,self.Fecha_Lanzamiento))
