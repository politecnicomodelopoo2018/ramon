from PyMySQL import DB
from Album import Album
from Artista import Artista
from Cancion import Cancion
from Genero import Genero



menu = {}
menu['1']="Insertar Artista"
menu['2']="Leer Artista"
menu['3']="Eliminar Artista"
menu['4']="Modificar Artista"
menu['5']="Insertar Album"
menu['6']="Leer Album"
menu['7']="Eliminar Album"
menu['8']="Modificar Album"
menu['9']="Insertar Cancion"
menu['10']="Leer Cancion"
menu['11']="Eliminar Cancion"
menu['12']="Modificar Cancion"
menu['13']="Insertar Genero"
menu['14']="Leer Genero"
menu['15']="Eliminar Genero"
menu['16']="Modificar Genero"
menu['17']="Exit"

a = 0

while a != '18':
    print('---------------MENU-------------')
    print('|             Artista          |')
    print('|         ---------------      |')
    print('|1)           Insertar         |')
    print('|2)             Leer           |')
    print('|3)           Eliminar         |')
    print('|4)           Modificar        |')
    print('|                              |')
    print('|              Album           |')
    print('|         ---------------      |')
    print('|5)           Insertar         |')
    print('|6)             Leer           |')
    print('|7)           Eliminar         |')
    print('|8)           Modificar        |')
    print('|                              |')
    print('|             Cancion          |')
    print('|         ---------------      |')
    print('|9)           Insertar         |')
    print('|10)            Leer           |')
    print('|11)          Eliminar         |')
    print('|12)          Modificar        |')
    print('|                              |')
    print('|              Genero          |')
    print('|         ---------------      |')
    print('|13)          Insertar         |')
    print('|14)         Unir Tablas       |')
    print('|15)            Leer           |')
    print('|16)          Eliminar         |')
    print('|17)          Modificar        |')
    print('|                              |')
    print('|18)            EXIT           |')
    print('--------------------------------')


    a = input("Porfavor Seleccione Numero:")

    if a =='1':
        p = Artista('NULL','NULL','NULL')
        banda = input("Ingrese Artista: ")
        concierto = input("Ingresar Concierto: ")
        p.InsertArt(banda,concierto)
    elif a =='2':
        p = Artista('NULL','NULL','NULL')
        z = p.LeerArt()
        for a in z:
            print(a.idArtista, " - ", a.Nombre, " - ", a.Conciertos)
    elif a =='3':
        p = Artista('NULL','NULL','NULL')
        id_borrar = input ("Ingrese ID a Borrar: ")
        p.BorrarArt(id_borrar)
    elif a =='4':
        p = Artista('NULL','NULL','NULL')
        id_update = input("Ingrese ID a Actualizar: ")
        nombre_nuevo = input("Ingrese Nombre a Actualizar: ")
        concierto_nuevo = input("Ingrese Concierto a Actualizar: ")
        p.ActualizarArt(nombre_nuevo,concierto_nuevo,id_update)
    elif a =='5':
        p = Album('NULL','NULL','NULL')
        nom_al = input("Ingrese Nombre Album: ")
        fech_lan = input("Ingresar Fecha de Lanazamiento: ")
        p.InsertAl(nom_al,fech_lan)
    elif a == '6':
        p = Album('NULL','NULL','NULL')
        z = p.LeerAl()
        for a in z:
            print(a.idAlbum, ' - ',a.Nombre_Album, " - ", a.Fecha_Lanzamiento)
    elif a =='7':
        p = Album('NULL','NULL','NULL')
        id_borrar = input ("Ingrese ID a Borrar: ")
        p.BorrarAl(id_borrar)
    elif a =='8':
        p = Album('NULL','NULL','NULL')
        id_update = input("Ingrese ID a Actualizar: ")
        nombre_nuevo = input("Ingrese nuevo Nombre: ")
        fecha_nuevo = input("Ingrese nuevo Fecha: ")
        p.ActualizarAl(nombre_nuevo,fecha_nuevo,id_update)
    elif a =='9':
        p = Cancion('NULL','NULL','NULL','NULL')
        id_Art = input("Ingrese ID del Artista de la Cancion: ")
        id_Al = input("Ingrese ID del Album de la Cancion: ")
        nom_can = input("Ingrese Nombre Cancion: ")
        p.InsertCan(nom_can,id_Art,id_Al)
    elif a == '10':
        p = Cancion('NULL','NULL','NULL','NULL')
        id_artis = input("Ingrese ID del Artista que hizo la Canciones: ")
        id_alb = input("Ingrese ID del Album donde van las Canciones: ")
        z = p.LeerCan(id_artis,id_alb)
        for a in z:
            print(a.idCancion, " - ",a.Nombre_Cancion, " - ", a.idCancion_Artista, " - ",a.idCancion_Album )
    elif a =='11':
        p = Cancion('NULL','NULL','NULL','NULL')
        id_borrar = input ("Ingrese ID a Borrar: ")
        p.BorrarCan(id_borrar)
    elif a =='12':
        p = Cancion('NULL','NULL','NULL','NULL')
        id_update = input("Ingrese ID a Actualizar: ")
        nombre_nuevo = input("Ingrese Cancion a Actualizar: ")
        p.ActualizarCan(nombre_nuevo,id_update)
    elif a =='13':
        p = Genero('NULL','NULL')
        nom_gen = input("Ingrese Genero: ")
        p.InsertGen(nom_gen)
    elif a == '14':
        id_album = input("Ingrese ID del Album: ")
        id_gen = input("Ingrese ID del Genero: ")
        DB.run("insert into Album_has_Genero values ('%s','%s')" % (id_album, id_gen))
    elif a == '15':

        id_alberto = input("Ingrese ID Album para Leer: ")
        z = Genero.LeerGen(id_alberto)
        for a in z:
            print(a.idGenero, " - ",a.Nombre_Genero)
    elif a =='16':
        p = Genero('NULL','NULL')
        id_borrar = input ("Ingrese ID a Borrar: ")
        p.BorrarGen(id_borrar)
    elif a =='17':
        p = Genero('NULL','NULL')
        id_update = input("Ingrese ID a Actualizar: ")
        nombre_nuevo = input("Ingrese Genero a Actualizar: ")
        p.ActualizarGen(nombre_nuevo,id_update)
