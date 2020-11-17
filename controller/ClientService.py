from domain.Client import Client
from domain.InstanceCounter import InstanceCounter
from exceptions.Exceptions import *

class ClientService:
    def __init__(self, repo, validare) -> None:
        self.__validare = validare
        self.__repo = repo
        self.__ic = InstanceCounter()


    def adaugare_client(self, nume, cnp):
        #Functie folosita pentru adaugarea clientului
        #Date de intrare: nume String, cnp String (0 -> 9)
        #Date de iesire: -
        client = Client(self.__ic.getNewClientId(), nume, cnp)
        #Creezi o instanta a obiectului
        #Validezi
        self.__validare.validare_client(client, self.__repo.get_lista_clienti())
        self.__ic.updateLastClientId()
        #Actualizam ultimul ID daca nu a crapat
        #Adaugi la lista
        self.__repo.adauga_client(client)


    def cauta_client(self, clientId):
        #Functie care cauta un clinet din repo
        #Date de intrare: clientId int
        #Date de iesire: True -> client gasit
        pass


    def cauta_client_nume(self, nume):
        #Functie care cauta un client din repo dupa nume
        #Date de intrare: nume String
        #Date de iesire: True -> Clinet gasit
        client = self.__repo.get_client_by_name(nume)
        if type(client) != Client:
            raise ClientNotFound
        return True


    