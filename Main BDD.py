from Album import Album
from Artista import Artista
from Cancion import Cancion
from Genero import Genero

p = Artista()

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
while True:

    selection=input("Please Select:")
    if selection =='1':
        p.InsertArt('Purpura','Condarco 2506')
    elif selection == '2':
        z = p.LeerArt()
        for a in z:
            print(a.Nombre, " - ", a.Conciertos)
    elif selection == '3':

    elif selection == '17':
      break
    else:
      print ("Unknown Option Selected!")
