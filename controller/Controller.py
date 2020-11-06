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
