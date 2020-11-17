from domain.Client import Client
from domain.Inchirieri import Inchirieri
from UI.UI import UI

class ClientRepo:
    def __init__(self):
        self.__listaClienti = []
        self.__inchirieri = Inchirieri()


    def adauga_client(self, client, ui=True):
        #Functie care adauga un client nou in repo
        #Date de intrare: client Client
        #Date de iesire: -
        self.__listaClienti.append(client)
        if ui: UI.display_client_added(client)


    def get_client_by_id(self, id):
        #Functie care cauta un client dupa ID
        #Date de intrare: id Int
        #Date de iesire: client Client / False pentru client inexistent
        for client in self.__listaClienti:
            if client.getId() == id:
                return client
        return False


    def get_client_by_name(self, name):
        #Functie care cauta un client dupa nume
        #Date de intrare: name String
        #Date de iesire: client Client / False pentru client inexistent
        for client in self.__listaClienti:
            if client.getName() == name:
                return client
        return False


    def get_client_by_cnp(self, cnp):
        #Functie care cauta un client dupa CNP
        #Date de intrare: cnp String
        #Date de iesire: client Client / False pentru client inexistent
        for client in self.__listaClienti:
            if client.getCnp() == cnp:
                return client
        return False


    def deleteClientFromList(self, clientToDelete, ui=True) -> None:
        #Functie care sterge un client din repo
        #Date de intrare: clientToDelete Client
        #Date de iesire: -
        idx = 0
        for index, client in enumerate(self.__listaClienti):
            if client.getId() == clientToDelete.getId():
                idx = index
                break
        del(self.__listaClienti[idx])
        if ui: UI.display_client_deleted_notification()


    def get_lista_clienti(self):
        #Functie care returneaza lista de clienti
        #Date intrare: -
        #Date de iesire: -
        return self.__listaClienti