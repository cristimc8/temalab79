from domain.Film import Film
from domain.InstanceCounter import InstanceCounter
from exceptions.Exceptions import *

class FilmService:
    def __init__(self, repo, valid) -> None:
        self.__validare = valid
        self.__repo = repo
        self.__ic = InstanceCounter()


    def adaugare_film(self, titlu, descriere, gen):
        #Functie folosita pentru adaugarea filmului
        #Date de intrare: titlu String, descriere String, gen String
        #Date de iesire: -
        film = Film(self.__ic.getNewFilmId(), titlu, descriere, gen)
        #Creezi o instanta a obiectului
        #Validezi
        self.__validare.validare_film(film)
        self.verifica_dublura_titlu(titlu)
        self.__ic.updateLastFilmId()
        #Actualizam ultimul ID al filmelor
        self.__repo.adauga_film(film)


    def modificare_film(self, id, titlu, descriere, gen):
        #Functie care modifica un film cu valori noi
        #Date de intrare: id Int, titlu String, descriere String, gen String
        #Date de iesire: -
        film = self.__repo.get_film_by_id(id)
        if type(film) != Film:
            raise FilmNotFound
        #Cream un film nou dupa cerintele filmului actualizat
        newFilm = Film(titlu, descriere, gen)
        self.__validare.validare_film(newFilm)
        self.verifica_dublura_titlu(titlu)
        #Daca este bun, actualizam filmul original
        film.updateTitlu(titlu)
        film.updateDescriere(descriere)
        film.updateGen(gen)
        self.__repo.updateFilmInList(film)


    def verifica_dublura_titlu(self, titlu):
        #Functie care arunca exceptie de tipul FilmAlreadyExists daca filmul cautat exista deja
        #Date de intrare: titlu String
        #Date de iesire: -
        filmSearch = self.exista_film_titlu(titlu)
        if filmSearch == True:
            raise FilmAlreadyExists
            


    def este_de_tip_film(self, film):
        #Functie care verifica daca un obiect 'film' este de tip Film
        #Date de intrare: film Obj
        #Date de iesire: Boolean
        return type(film) == Film


    def modificare_client(self, id, nume, cnp):
        #Functie care modifica un client cu valori noi
        #Date de intrare: id Int, nume String, cnp String(0 -> 9)
        #Date de iesire: -
        pass


    def cauta_film(self, filmId):
        #Functie care cauta un film din repo
        #Date de intrare: filmId int
        #Date de iesire: filmGasit Film
        filmGasit = self.__repo.get_film_by_id(filmId)
        if self.este_de_tip_film(filmGasit):
            return filmGasit
        return None


    def exista_film_titlu(self, titlu):
        #Functie care cauta un film din repo
        #Date de intrare: filmId int
        #Date de iesire: True -> film gasit
        filmGasit = self.__repo.get_film_by_title(titlu)
        return self.este_de_tip_film(filmGasit)


    def cauta_film_titlu(self, filmName):
        #Functie care cauta un film din repo dupa nume
        #Date de intrare: filmName String
        #Date de iesire: filmGasit Film
        filmGasit = self.__repo.get_film_by_title(filmName)
        if self.este_de_tip_film(filmName):
            return filmGasit
        return None


    def sterge_film(self, id):
        #Functie care sterge filmul din repo
        #Date de intrare: id Int
        #Date de iesire: -
        film = self.__repo.get_film_by_id(id)
        if not self.este_de_tip_film(film):
            raise FilmNotFound
        self.__repo.deleteFilmFromList(film)


    def display_all_films(self):
        #Functie care arata toate filmele din repo
        #Date de intrare: -
        #Date de iesire: -
        self.__repo.display_all_films()


    def inchiriaza_film(self, clientName, filmTitle):
        if self.cauta_client_nume(clientName) == True and self.cauta_film_titlu(filmTitle) == True:
            client = self.__repo.get_client_by_name(clientName)
            film = self.__repo.get_film_by_title(filmTitle)
            self.__repo.adauga_inchiriere(client, film)


    def afiseaza_inchirieri(self, client):
        clientT = self.__repo.get_client_by_name(client)
        filmInchiriat = self.__repo.get_inchirieri(clientT)
        listaFilme = []
        for film in filmInchiriat:
            listaFilme.append(film.getTitlu())
        #UI.afiseaza_inchirieri(listaFilme)
        #De sters de aici