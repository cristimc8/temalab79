from domain.Film import Film
from domain.Client import Client

class Repo:
    def __init__(self):
        self.__listaFilme = []
        self.__listaClienti = []


    def print_lista_clienti(self):
        for client in self.__listaClienti:
            print(str(client) + '\n')


    def adauga_film(self, film):
        self.__listaFilme.append(film)


    def adauga_client(self, client):
        self.__listaClienti.append(client)


    def get_film_by_id(self, id):
        for film in self.__listaFilme:
            if film.getId() == id:
                return film
        return False


    def updateFilmInList(self, newFilm):
        for index, film in enumerate(self.__listaFilme):
            if film.getId() == newFilm.getId():
                self.__listaFilme[index] = newFilm
            

    def deleteFilmFromList(self, filmToDelete):
        idx = 0
        for index, film in enumerate(self.__listaFilme):
            if film.getId() == filmToDelete.getId():
                idx = index
                break
        del(self.__listaFilme[idx])


    def get_lista_filme(self):
        return self.__listaFilme

    
    def get_lista_clienti(self):
        return self.__listaClienti