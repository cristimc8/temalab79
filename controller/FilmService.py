from domain.Film import Film
from domain.InstanceCounter import InstanceCounter
from exceptions.Exceptions import *
from random_generator.RandomFill import RandomFill

class FilmService:
    def __init__(self, repo, valid) -> None:
        self.__validare = valid
        self.__repo = repo
        self.__ic = InstanceCounter()
        self.__rand = RandomFill()


    def adauga_random(self, n):
        self.__rand.get_random_films(n)
        for index, el in enumerate(self.__rand.filmTitles):
            self.adaugare_film(self.__rand.filmTitles[index], self.__rand.filmDescriptions[index], self.__rand.filmGenres[index])


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
        return film


    def modificare_film(self, id, titlu, descriere, gen):
        #Functie care modifica un film cu valori noi
        #Date de intrare: id Int, titlu String, descriere String, gen String
        #Date de iesire: -
        film = self.get_film_by_id(id)
        if type(film) != Film:
            raise FilmNotFound
        #Cream un film nou dupa cerintele filmului actualizat
        newFilm = Film(id, titlu, descriere, gen)
        self.__validare.validare_film(newFilm)
        self.verifica_dublura_titlu(titlu)
        #Daca este bun, actualizam filmul original
        film.updateTitlu(titlu)
        film.updateDescriere(descriere)
        film.updateGen(gen)
        self.__repo.updateFilmInList(film)
        return film


    def verifica_dublura_titlu(self, titlu):
        #Functie care arunca exceptie de tipul FilmAlreadyExists daca filmul cautat exista deja
        #Date de intrare: titlu String
        #Date de iesire: -
        filmSearch = self.exista_film_titlu(titlu)
        if filmSearch == True:
            raise FilmAlreadyExists


    def cautare_dupa_id(self, id):
        #Functia care returneaza un obiect de tip Film dupa un id
        #Date de intare: id Int
        #Date de iesire: film Film
        try:
            id = int(id)
        except:
            raise IdIsNotNumber
        film = self.get_film_by_id(id)
        if type(film) != Film:
            raise FilmNotFound
        return film
            


    def este_de_tip_film(self, film):
        #Functie care verifica daca un obiect 'film' este de tip Film
        #Date de intrare: film Obj
        #Date de iesire: Boolean
        return type(film) == Film


    def get_film_by_id(self, id):
            #Functie care cauta un film dupa ID
            #Date de intrare: id Int
            #Date de iesire: film Film / False pentru film inexistent
            try:
                id = int(id)
            except:
                raise IdIsNotNumber
            listaFilme = self.__repo.get_lista_filme()
            for film in listaFilme:
                if film.getId() == id:
                    return film
            return False

    
    def get_film_by_title(self, title):
        #Functie care cauta un film dupa titlu
        #Date de intrare: title String
        #Date de iesire: film Film / False pentru film inexistent
        listaFilme = self.__repo.get_lista_filme()
        for film in listaFilme:
            if film.getTitlu() == title:
                return film
        return False


    def exista_film_titlu(self, titlu):
        #Functie care cauta un film din repo
        #Date de intrare: filmId int
        #Date de iesire: True -> film gasit
        filmGasit = self.get_film_by_title(titlu)
        return self.este_de_tip_film(filmGasit)


    def sterge_film(self, id):
        #Functie care sterge filmul din repo
        #Date de intrare: id Int
        #Date de iesire: -
        film = self.get_film_by_id(id)
        if not self.este_de_tip_film(film):
            raise FilmNotFound
        self.__repo.deleteFilmFromList(film)


    def display_all_films(self):
        #Functie care arata toate filmele din repo
        #Date de intrare: -
        #Date de iesire: -
        return self.__repo.get_lista_filme()