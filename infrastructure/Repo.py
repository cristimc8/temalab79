from domain.Film import Film
from domain.Client import Client

class Repo:
    def __init__(self):
        self.__listaFilme = []
        self.__listaClienti = []


    def print_lista_clienti(self):
        for client in self.__listaClienti:
            print(str(client) + '\n')


    def adauga_film(self):
        pass


    def adauga_client(self, client):
        self.__listaClienti.append(client)
        self.print_lista_clienti()
