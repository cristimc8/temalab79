class Inchirieri:
    def __init__(self) -> None:
        self.__colectie = {}


    def inchiriaza(self, client, film):
        self.__colectie[client] = []
        self.__colectie[client].append(film)


    def get_filme_inchiriate(self, client):
        return self.__colectie[client]


    def stergeInchiriere(self, client, film):
        self.__colectie[client].remove(film)