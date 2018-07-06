
from MySQL import DB
from Artista import Artista

c=DB.run("select * from Artista")

for b in c:
    unArtista = Artista
    unArtista.idArtist=b['idArtista']
    unArtista.Nombre=b['Nombre']
    unArtista.Apellido=b['Apellido']
    unArtista.Conciertos=b['Conciertos']