from domain.Client import Client
from domain.Film import Film
from domain.InstanceCounter import InstanceCounter
from exceptions.Exceptions import *
from UI.UI import UI
class Controller:
    def __init__(self, validare_client, repo):
        self.__validare = validare_client
        self.__repo = repo
        self.__ic = InstanceCounter()


    def adaugare_client(self, nume, cnp):
        client = Client(self.__ic.getNewClientId(), nume, cnp)
        #Creezi o instanta a obiectului
        #Validezi
        try:
            self.__validare.validare_client(client, self.__repo.get_lista_clienti())
        except (CnpNotValid, CnpNotNumber, CnpAlreadyExists) as exc:
            UI.CnpNotValid(client.getCnp(), exc)
            self.__ic.popClientId()
            return False
        #Adaugi la lista
        self.__repo.adauga_client(client)
        UI.display_client_added(client)
        return True
        

    def adaugare_film(self, titlu, descriere, gen):
        film = Film(self.__ic.getNewFilmId(), titlu, descriere, gen)
        try:
            self.__validare.validare_film(film, self.__repo.get_lista_filme())
        except (FilmAlreadyExists) as exc:
            UI.FilmAlreadyExists(film.getTitlu(), exc)
            self.__ic.popFilmId()
            return False
        self.__repo.adauga_film(film)
        UI.display_film_added(film)
        return True


    def modificare_film(self, id, titlu, descriere, gen):
            film = self.__repo.get_film_by_id(id)
            if type(film) != Film:
                UI.display_missing_film_error(id)
                return False
            film.updateTitlu(titlu)
            film.updateDescriere(descriere)
            film.updateGen(gen)
            self.__repo.updateFilmInList(film)
            UI.display_film_updated(film)


    def modificare_client(self, id, nume, cnp):
        pass


    def sterge_client(self, id):
        pass


    def cauta_film(self, titlu):
        pass


    def cauta_client(self, nume):
        pass


    def sterge_film(self, id):
        film = self.__repo.get_film_by_id(id)
        if type(film) != Film:
            UI.display_missing_film_error(id)
            return False
        self.__repo.deleteFilmFromList(film)
        UI.display_film_deleted_notification()


    def display_all_films(self):
        for film in self.__repo.get_lista_filme():
            UI.display_film(film)