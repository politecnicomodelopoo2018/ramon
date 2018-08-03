from Album import Album
from Artista import Artista
from Cancion import Cancion
from Genero import Genero

p = Artista('Purpura','Cabildo 2506 - 25/09')

z = p.LeerArt()
for a in z:
    print(a.Nombre, " - ",a.Conciertos)