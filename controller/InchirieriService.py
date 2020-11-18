from domain.Inchirieri import Inchirieri
from exceptions.Exceptions import *

class InchirieriService:
    def __init__(self, repo, clientService, filmService) -> None:
        self.__clientService = clientService
        self.__filmService = filmService
        self.__repo = repo
    

    def adaugare_inchiriere(self, idC, idF):
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
        listaInchirieri = self.get_inchirieri_nereturnate()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm() == film:
                return True
        return False


    def get_inchirieri_client(self, client):
        listaInchirieriClient = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getClient() == client:
                listaInchirieriClient.append(inchiriere)
        return listaInchirieriClient


    def get_inchirieri_film(self, film):
        listaCarti = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm() == film:
                listaCarti.append(inchiriere)
        return listaCarti


    def get_inchirieri_nereturnate(self):
        listaInchirieriNereturnate = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.isReturnat() == False:
                listaInchirieriNereturnate.append(inchiriere)
        return listaInchirieriNereturnate


    def arata_inchirieri(self):
        self.__repo.display_all_inchireri()
