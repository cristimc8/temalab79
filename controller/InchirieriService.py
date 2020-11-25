from domain.Inchirieri import Inchirieri
from exceptions.Exceptions import *
import math

class InchirieriService:
    def __init__(self, repo, clientService, filmService) -> None:
        self.__clientService = clientService
        self.__filmService = filmService
        self.__repo = repo
    

    def adaugare_inchiriere(self, idC, idF):
        #Functia care adauga o inchiriere in lista din repo
        #Date de intrare: idC Int idF Int
        #Date de iesire: inchirierie Inchirieri
        client = self.__clientService.get_client_by_id(idC)
        if type(client) == bool:
            raise ClientNotFound
        film = self.__filmService.get_film_by_id(idF)
        if type(film) == bool:
            raise FilmNotFound

        inchiriere = Inchirieri(client, film)
        if self.este_inchiriat(film):
            raise FilmDejaInchiriat
        self.__repo.adauga_inchiriere(inchiriere)
        return inchiriere

    
    def returneaza_inchiriere(self, idC, idF):
        #Functia care face ca un client sa returneze un film si ca acesta sa figureze ca "returnat"
        #Date de intrare: idC Int idF Int
        #Date de iesire: -
        client = self.__clientService.get_client_by_id(idC)
        if type(client) == bool:
            raise ClientNotFound
        film = self.__filmService.get_film_by_id(idF)
        if type(film) == bool:
            raise FilmNotFound

        for inchiriere in self.get_inchirieri_nereturnate():
            if inchiriere.getFilm() == film:
                inchiriere.returneaza()
                return True
        raise FilmNuEsteInchiriat


    def este_inchiriat(self, film):
        #Functia care verifica daca un film este inchiriat
        #Date de intrare: film Film
        listaInchirieri = self.get_inchirieri_nereturnate()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm() == film:
                return True
        return False


    def get_inchirieri_client(self, client):
        #Functia care returneaza o lista cu toate inchirierile unui client
        #Date de intrare: client Client
        #Date de iesire: lista List
        listaInchirieriClient = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getClient() == client:
                listaInchirieriClient.append(inchiriere)
        return listaInchirieriClient


    def get_inchirieri_film(self, film):
        #Functia care returneaza lista cu inchirirerile unui film
        #Date de intrare: film Film
        #Date de iesire: -
        listaFilme = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm() == film:
                listaFilme.append(inchiriere)
        return listaFilme


    def get_inchirieri_nereturnate(self):
        #Functia care returneaza lista cu inchirierile care nu sunt returnate inca
        #Date de intrare: -
        #Date de iesire: -
        listaInchirieriNereturnate = []
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.isReturnat() == False:
                listaInchirieriNereturnate.append(inchiriere)
        return listaInchirieriNereturnate


    def get_clients_ordered_by_name(self):
        #Functia care returneaza lista de inchirireri ordonata alfabetic dupa clienti
        #Date de intrare: -
        #Date de iesire: list(Inchireri)
        listaInchirieri = self.__repo.get_lista_inchirieri()
        listaOrdonataDupaNume = listaInchirieri.copy()
        ordonat = False
        while(not ordonat):
            ordonat = True
            for index, inchiriere in enumerate(listaOrdonataDupaNume):
                if index == len(listaOrdonataDupaNume) - 1: break
                if inchiriere.getClient().getName()[0] > listaOrdonataDupaNume[index + 1].getClient().getName()[0]:
                    ordonat = False
                    listaOrdonataDupaNume[index], listaOrdonataDupaNume[index + 1] = listaOrdonataDupaNume[index + 1], listaOrdonataDupaNume[index]
        return listaOrdonataDupaNume


    def count_film_occurence(self, film):
        #Functia care numara de cate ori apare un film in lista de inchirieri
        #Date de intrare: film Film
        #Date de iesire: occurence Int
        occurence = 0
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getFilm().getId() == film.getId():
                occurence += 1
        return occurence


    def count_client_occurence(self, client):
        #Functia care numara de cate ori apare un client in lista de inchirireri
        #Date de intrare: client Client
        #Date de iesire: occurence Int
        occurence = 0
        listaInchirieri = self.__repo.get_lista_inchirieri()
        for inchiriere in listaInchirieri:
            if inchiriere.getClient().getId() == client.getId():
                occurence += 1
        return occurence


    def get_clienti_ordonat_dupa_filme_inchiriate(self):
        #Functia care returneaza cei mai activi clienti dupa inchirieri
        #Date de intrare: -
        #Date de iesire: Dict(String, occurence Int)
        listaInchirieri = self.__repo.get_lista_inchirieri()
        listaOrdonata = listaInchirieri.copy()
        #Bubble sort
        ordered = False
        while not ordered:
            ordered = True
            for index, inchiriere in enumerate(listaOrdonata):
                if index == len(listaOrdonata) - 1: break
                if self.count_client_occurence(inchiriere.getClient()) < self.count_client_occurence(listaOrdonata[index + 1].getClient()):
                    listaOrdonata[index], listaOrdonata[index + 1] = listaOrdonata[index + 1], listaOrdonata[index]
        listaClienti = {}
        for inchiriere in listaOrdonata:
            listaClienti[inchiriere.getClient().getName()] = self.count_client_occurence(inchiriere.getClient())
        #Lambda function, reverse the dictionary
        listaClienti = dict(reversed(sorted(listaClienti.items(), key=lambda item: item[1])))
        return listaClienti


    def get_primii_30perc_clienti(self):
        #Functia care returneaza primii 30% clienti in functie de nr de filme inchiriate
        #Date de intrare: -
        #Date de iesire: Dict(String, occurence Int)
        listaFullClientiOrdonata = self.get_clienti_ordonat_dupa_filme_inchiriate()
        #30% din lista = 3/10 din aia
        #3/10 * len(lista) doar
        neededLength = math.ceil(3/10 * len(listaFullClientiOrdonata))
        return {k: listaFullClientiOrdonata[k] for k in list(listaFullClientiOrdonata)[:neededLength]}


    def get_clienti_intre_medii(self, min, max):
        listaInchirieri = self.__repo.get_lista_inchirieri()
        listaOrdonata = []
        for index, inchiriere in enumerate(listaInchirieri):
            if self.count_client_occurence(inchiriere.getClient()) <= max and self.count_client_occurence(inchiriere.getClient()) >= min:
                listaOrdonata.append(inchiriere)
        listaClienti = {}
        for inchiriere in listaOrdonata:
            listaClienti[inchiriere.getClient().getName()] = self.count_client_occurence(inchiriere.getClient())
        #Lambda function, reverse the dictionary
        listaClienti = dict(reversed(sorted(listaClienti.items(), key=lambda item: item[1])))
        return listaClienti

    #Clientii cu nr minim si maxim de inchirieri


    def get_cele_mai_inchiriate(self):
        #Functia care returneaza cele mai inchiriate filme din repo, ordonate descrescator
        #Date de intrare: -
        #Date de iesire: Dict(String, occurence Int)
        listaInchirieri = self.__repo.get_lista_inchirieri()
        listaOrdonate = listaInchirieri.copy()
        #Bubble sort
        ordered = False
        while not ordered:
            ordered = True
            for index, inchiriere in enumerate(listaOrdonate):
                if index == len(listaOrdonate) - 1: break
                if self.count_film_occurence(inchiriere.getFilm()) < self.count_film_occurence(listaOrdonate[index + 1].getFilm()):
                    listaOrdonate[index], listaOrdonate[index + 1] = listaOrdonate[index + 1], listaOrdonate[index]
        listaFilme = {}
        for inchiriere in listaOrdonate:
            listaFilme[inchiriere.getFilm().getTitlu()] = self.count_film_occurence(inchiriere.getFilm())
        #Lambda function, reverse the dictionary
        listaFilme = dict(reversed(sorted(listaFilme.items(), key=lambda item: item[1])))
        return listaFilme
        #[titanic, geon, titanic]



    def arata_inchirieri(self):
        #Functia care returneaza toate inchirierile
        return self.__repo.get_lista_inchirieri()
