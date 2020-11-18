from UI.UI import UI

class ClientRepo:
    def __init__(self):
        self.__listaClienti = []


    def adauga_client(self, client, ui=True):
        #Functie care adauga un client nou in repo
        #Date de intrare: client Client
        #Date de iesire: -
        self.__listaClienti.append(client)
        if ui: UI.display_client_added(client)


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
        return list(self.__listaClienti)


    def display_all_clients(self):
        #Functie care display-uieste toate filmele din repo
        #Date de intrare: -
        #Date de iesire: -
        for client in self.get_lista_clienti():
            UI.display_client(client)

    
    def updateClientInList(self, newClient, ui=True):
        #Functie care actualizeaza un client din repo cu date noi
        #Date de intrare: newClient Client
        #Date de iesire: -
        for index, client in enumerate(self.__listaClienti):
            if client.getId() == newClient.getId():
                self.__listaClienti[index] = newClient
        if ui: UI.display_client_updated(newClient)