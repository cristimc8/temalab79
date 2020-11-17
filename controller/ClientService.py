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
        self.__validare.validare_client(client)
        self.verifica_dublura_cnp(cnp)
        #Actualizam ultimul ID daca nu a crapat
        self.__ic.updateLastClientId()
        #Adaugi la lista
        self.__repo.adauga_client(client)


    def verifica_dublura_cnp(self, cnp):
        #Functie care arunca exceptie de tipul CnpAlreadyExists daca clientul cautat exista deja
        #Date de intrare: cnp String
        #Date de iesire: -
        newClient = self.exista_client_cnp(cnp)
        if newClient == True:
            raise CnpAlreadyExists


    def cauta_client(self, clientId):
        #Functie care cauta un clinet din repo
        #Date de intrare: clientId int
        #Date de iesire: client Client -> client gasit
        client = self.__repo.get_client_by_id(clientId)
        if self.este_de_tip_client(client):
            return client
        return None


    def exista_client_cnp(self, cnp):
        #Functie care cauta un client din repo dupa cnp
        #Date de intrare: cnp String
        #Date de iesire: True -> client gasit
        client = self.__repo.get_client_by_cnp(cnp)
        return self.este_de_tip_client(client)

    def cauta_client_cnp(self, cnp):
        #Functie care cauta un client din repo dupa cnp
        #Date de intrare: cnp String
        #Date de iesire: client Client -> client gasit
        client = self.__repo.get_client_by_cnp(cnp)
        if self.este_de_tip_client(client):
            return client
        return None
        

    def este_de_tip_client(self, client):
        #Functie care verifica daca un obiect 'client' este de tip Client
        #Date de intrare: client Obj
        #Date de iesire: Boolean
        return type(client) == Client


    def cauta_client_nume(self, nume):
        #Functie care cauta un client din repo dupa nume
        #Date de intrare: nume String
        #Date de iesire: client Client -> Client gasit
        client = self.__repo.get_client_by_name(nume)
        if self.este_de_tip_client(client):
            return client
        return None


    def sterge_client(self, id):
        #Functie care sterge clientul din repo
        #Date de intrare: id Int
        #Date de iesire: -
        client = self.__repo.get_client_by_id(id)
        if not self.este_de_tip_client(client):
            raise ClientNotFound
        self.__repo.deleteClientFromList(client)

    