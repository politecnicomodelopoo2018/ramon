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



a=input("Porfavor Seleccione Numero:")

if a =='1':
    p = Artista('NULL','NULL')
    banda = input("Ingrese Artista: ")
    concierto = input("Ingresar Concierto: ")
    p.InsertArt(banda,concierto)
elif a =='2':
    p = Artista('NULL','NULL')
    z = p.LeerArt()
    for a in z:
        print(a.Nombre, " - ", a.Conciertos)
elif a =='5':
    p = Album("NULL","NULL")
    nom_al = input("Ingrese Nombre Album: ")
    fech_lan = input("Ingresar Fecha de Lanazamiento: ")
    p.InsertAl(nom_al,fech_lan)
elif a == '6':
    p = Album('NULL','NULL')
    z = p.LeerAl()
    for a in z:
        print(a.Nombre_Album, " - ", a.Fecha_Lanzamiento)
elif a =='9':
    p = Cancion("NULL")
    nom_can = input("Ingrese Nombre Cancion: ")
    p.InsertCan(nom_can)
elif a == '10':
    p = Cancion('NULL')
    z = p.LeerCan()
    for a in z:
        print(a.Nombre_Cancion)
elif a =='13':
    p = Genero("NULL")
    nom_gen = input("Ingrese Genero: ")
    p.InsertGen(nom_gen)
elif a == '14':
    p = Genero('NULL')
    z = p.LeerGen()
    for a in z:
        print(a.Nombre_Genero)

