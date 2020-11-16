from domain.Film import Film
from domain.Client import Client
from domain.Inchirieri import Inchirieri
from UI.UI import UI

class Repo:
    def __init__(self):
        self.__listaFilme = []
        self.__listaClienti = []
        self.__inchirieri = Inchirieri()


    def adauga_film(self, film):
        #Functie care adauga un film nou in repo
        #Date de intrare: film Film
        #Date de iesire: -
        self.__listaFilme.append(film)
        UI.display_film_added(film)


    def display_all_films(self):
        #Functie care display-uieste toate filmele din repo
        #Date de intrare: -
        #Date de iesire: -
        for film in self.get_lista_filme():
            UI.display_film(film)


    def adauga_client(self, client):
        #Functie care adauga un client nou in repo
        #Date de intrare: client Client
        #Date de iesire: -
        self.__listaClienti.append(client)
        UI.display_client_added(client)


    def get_film_by_id(self, id):
        #Functie care cauta un film dupa ID
        #Date de intrare: id Int
        #Date de iesire: film Film / False pentru film inexistent
        for film in self.__listaFilme:
            if film.getId() == id:
                return film
        return False


    def get_client_by_id(self, id):
        #Functie care cauta un client dupa ID
        #Date de intrare: id Int
        #Date de iesire: client Client / False pentru client inexistent
        for client in self.__listaClienti:
            if client.getId() == id:
                return client
        return False


    def get_film_by_title(self, title):
        #Functie care cauta un film dupa titlu
        #Date de intrare: title String
        #Date de iesire: film Film / False pentru film inexistent
        for film in self.__listaFilme:
            if film.getTitlu() == title:
                return film
        return False


    def get_client_by_name(self, name):
        #Functie care cauta un client dupa nume
        #Date de intrare: name String
        #Date de iesire: client Client / False pentru client inexistent
        for client in self.__listaClienti:
            if client.getName() == name:
                return client
        return False


    def updateFilmInList(self, newFilm):
        #Functie care actualizeaza un film din repo cu date noi
        #Date de intrare: newFilm Film
        #Date de iesire: -
        for index, film in enumerate(self.__listaFilme):
            if film.getId() == newFilm.getId():
                self.__listaFilme[index] = newFilm
        UI.display_film_updated(newFilm)


    def deleteFilmFromList(self, filmToDelete):
        #Functie care sterge un film din repo
        #Date de intrare: filmToDelete Film
        #Date de iesire: -
        idx = 0
        for index, film in enumerate(self.__listaFilme):
            if film.getId() == filmToDelete.getId():
                idx = index
                break
        del(self.__listaFilme[idx])
        UI.display_film_deleted_notification()


    def get_lista_filme(self):
        #Functie care returneaza lista de filme din repo
        #Date de intrare: -
        #Date de iesire: -
        return self.__listaFilme

    
    def get_lista_clienti(self):
        #Functie care returneaza lista de clienti
        #Date intrare: -
        #Date de iesire: -
        return self.__listaClienti


    def adauga_inchiriere(self, client, film):
        self.__inchirieri.inchiriaza(client.getId(), film.getId())


    def get_inchirieri(self, client):
        lista = []
        for el in self.__inchirieri.get_filme_inchiriate(client.getId()):
            lista.append(self.get_film_by_id(el))
        return lista