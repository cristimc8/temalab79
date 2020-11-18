from domain.Inchirieri import Inchirieri
from exceptions.Exceptions import *

class InchirieriService:
    def __init__(self, repo, clientService, filmService) -> None:
        self.__clientService = clientService
        self.__filmService = filmService
        self.__repo = repo
    

    def adaugare_inchiriere(self, idC, idF):
        #Functia care adauga o inchiriere in lista din repo
        #Date de intrare: idC Int idF Int
        #Date de iesire: inchirierie Inchirieri
        client = self.__clientService.get_client_by_id(idC)
        if type(client) == bool:
            raise ClientNotFound
        film = self.__filmService.get_film_by_id(idF)
        if type(film) == bool:
            raise FilmNotFound

        inchiriere = Inchirieri(client, film)
        if self.este_inchiriat(film):
            raise FilmDejaInchiriat
        self.__repo.adauga_inchiriere(inchiriere)
        return inchiriere

    
    def returneaza_inchiriere(self, idC, idF):
        #Functia care face ca un client sa returneze un film si ca acesta sa figureze ca "returnat"
        #Date de intrare: idC Int idF Int
        #Date de iesire: -
        client = self.__clientService.get_client_by_id(idC)
        if type(client) == bool:
            raise ClientNotFound
        film = self.__filmService.get_film_by_id(idF)
        if type(film) == bool:
            raise FilmNotFound

        for inchiriere in self.get_inchirieri_nereturnate():
            if inchiriere.getFilm() == film:
                inchiriere.returneaza()
                return True
        raise FilmNuEsteInchiriat


    def este_inchiriat(self, film):
        #Functia care verifica daca un film este inchiriat
        #Date de intrare: film Film
        listaInchirieri = self.get_inchirieri_nereturnate()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm() == film:
                return True
        return False


    def get_inchirieri_client(self, client):
        #Functia care returneaza o lista cu toate inchirierile unui client
        #Date de intrare: client Client
        #Date de iesire: lista List
        listaInchirieriClient = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getClient() == client:
                listaInchirieriClient.append(inchiriere)
        return listaInchirieriClient


    def get_inchirieri_film(self, film):
        #Functia care returneaza lista cu inchirirerile unui film
        #Date de intrare: film Film
        #Date de iesire: -
        listaFilme = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm() == film:
                listaFilme.append(inchiriere)
        return listaFilme


    def get_inchirieri_nereturnate(self):
        #Functia care returneaza lista cu inchirierile care nu sunt returnate inca
        #Date de intrare: -
        #Date de iesire: -
        listaInchirieriNereturnate = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.isReturnat() == False:
                listaInchirieriNereturnate.append(inchiriere)
        return listaInchirieriNereturnate


    def arata_inchirieri(self):
        #Functia care returneaza toate inchirierile
        return self.__repo.get_lista_inchirieri()
