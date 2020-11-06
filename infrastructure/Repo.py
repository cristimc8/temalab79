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
        #raise defapt in controller


    def get_lista_filme(self):
        return self.__listaFilme

    
    def get_lista_clienti(self):
        return self.__listaClienti