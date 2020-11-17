from domain.Inchirieri import Inchirieri
from UI.UI import UI

class FilmRepo:
    def __init__(self):
        self.__listaFilme = []
        self.__inchirieri = Inchirieri()

    
    def adauga_film(self, film, ui=True):
        #Functie care adauga un film nou in repo
        #Date de intrare: film Film
        #Date de iesire: -
        self.__listaFilme.append(film)
        if ui: UI.display_film_added(film)


    def display_all_films(self):
        #Functie care display-uieste toate filmele din repo
        #Date de intrare: -
        #Date de iesire: -
        for film in self.get_lista_filme():
            UI.display_film(film)

    
    def get_film_by_id(self, id):
        #Functie care cauta un film dupa ID
        #Date de intrare: id Int
        #Date de iesire: film Film / False pentru film inexistent
        for film in self.__listaFilme:
            if film.getId() == id:
                return film
        return False

    
    def get_film_by_title(self, title):
        #Functie care cauta un film dupa titlu
        #Date de intrare: title String
        #Date de iesire: film Film / False pentru film inexistent
        for film in self.__listaFilme:
            if film.getTitlu() == title:
                return film
        return False


    def updateFilmInList(self, newFilm, ui=True):
        #Functie care actualizeaza un film din repo cu date noi
        #Date de intrare: newFilm Film
        #Date de iesire: -
        for index, film in enumerate(self.__listaFilme):
            if film.getId() == newFilm.getId():
                self.__listaFilme[index] = newFilm
        if ui: UI.display_film_updated(newFilm)


    def deleteFilmFromList(self, filmToDelete, ui=True) -> None:
        #Functie care sterge un film din repo
        #Date de intrare: filmToDelete Film
        #Date de iesire: -
        idx = 0
        for index, film in enumerate(self.__listaFilme):
            if film.getId() == filmToDelete.getId():
                idx = index
                break
        del(self.__listaFilme[idx])
        if ui: UI.display_film_deleted_notification()


    def get_lista_filme(self):
        #Functie care returneaza lista de filme din repo
        #Date de intrare: -
        #Date de iesire: -
        return self.__listaFilme