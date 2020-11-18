from UI.UI import UI

class InchirieriRepo:
    def __init__(self) -> None:
        self.__listaInchirieri = []


    def adauga_inchiriere(self, inchiriere, ui=True):
        '''
        Functia care adauga o inchiriere noua in lista
        in -> client Client, film Film
        '''
        self.__listaInchirieri.append(inchiriere)
        if ui: UI.display_inchiriere(inchiriere)


    def sterge_inchiriere(self, inchiriere):
        '''
        Functia care sterge inchirierea din lista daca utilizatorul isi sterge contul
        '''
        self.__listaInchirieri.remove(inchiriere)


    def get_inchiriere_client(self, client):
        listaInchirieri = []
        for inchiriere in self.__listaInchirieri:
            if inchiriere.getClient() == client:
                listaInchirieri.append(inchiriere)
        return listaInchirieri
    

    def get_inchirieri_film(self, film):
        listaInchirieri = []
        for inchiriere in self.__listaInchirieri:
            if inchiriere.getFilm() == film:
                listaInchirieri.append(inchiriere)
        return listaInchirieri

    
    def get_lista_inchirieri(self):
        return list(self.__listaInchirieri)


    def display_all_inchireri(self):
        for inchiriere in self.__listaInchirieri:
            UI.display_inchiriere(inchiriere)
