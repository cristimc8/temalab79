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
        return client


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
        try:
            clientId = int(clientId)
        except:
            raise IdIsNotNumber
        client = self.get_client_by_id(clientId)
        if self.este_de_tip_client(client):
            return client
        return None


    def display_all_clients(self):
        #Functie care arata toti clientii
        #self.__repo.display_all_clients()
        return self.__repo.get_lista_clienti()

        
    def get_client_by_id(self, id):
        #Functie care cauta un client dupa ID
        #Date de intrare: id Int
        #Date de iesire: client Client / False pentru client inexistent
        try:
            id = int(id)
        except:
            raise IdIsNotNumber
        listaClienti = self.__repo.get_lista_clienti()
        for client in listaClienti:
            print(client.getId())
            if client.getId() == id:
                return client
        return False


    def get_client_by_name(self, name):
        #Functie care cauta un client dupa nume
        #Date de intrare: name String
        #Date de iesire: client Client / False pentru client inexistent
        listaClienti = self.__repo.get_lista_clienti()
        for client in listaClienti:
            if client.getName() == name:
                return client
        return False


    def get_client_by_cnp(self, cnp):
        #Functie care cauta un client dupa CNP
        #Date de intrare: cnp String
        #Date de iesire: client Client / False pentru client inexistent
        listaClienti = self.__repo.get_lista_clienti()
        for client in listaClienti:
            if client.getCnp() == cnp:
                return client
        return False


    def exista_client_cnp(self, cnp):
        #Functie care cauta un client din repo dupa cnp
        #Date de intrare: cnp String
        #Date de iesire: True -> client gasit
        client = self.get_client_by_cnp(cnp)
        return self.este_de_tip_client(client)
        

    def este_de_tip_client(self, client):
        #Functie care verifica daca un obiect 'client' este de tip Client
        #Date de intrare: client Obj
        #Date de iesire: Boolean
        return type(client) == Client


    def modificare_client(self, id, nume, cnp):
        #Functie care modifica un film cu valori noi
        #Date de intrare: id Int, titlu String, descriere String, gen String
        #Date de iesire: -
        client = self.get_client_by_id(id)
        if type(client) != Client:
            raise ClientNotFound
        #Cream un clinet nou dupa cerintele clientului actualizat
        newClient = Client(id, nume, cnp)
        self.__validare.validare_client(newClient)
        self.verifica_dublura_cnp(cnp)
        #Daca este bun, actualizam clientul original
        client.updateNume(nume)
        client.updateCnp(cnp)
        self.__repo.updateClientInList(client)
        return client


    def sterge_client(self, id):
        #Functie care sterge clientul din repo
        #Date de intrare: id Int
        #Date de iesire: -
        client = self.get_client_by_id(id)
        if not self.este_de_tip_client(client):
            raise ClientNotFound
        self.__repo.deleteClientFromList(client)

    