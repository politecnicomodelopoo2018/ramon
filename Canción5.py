from Artista5 import Artista
from Autor5 import Autor

class Cancion(object):
    Titulo=None

    def __init__(self, Tit):
        self.Lista_Artista=[]
        self.Lista_Autor=[]
        self.Titulo=Tit
