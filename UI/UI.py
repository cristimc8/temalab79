class UI:
    def __init__(self):
        pass


    @staticmethod
    def show_film(film):
        '''
        Metoda primeste ca argument un film de tip Film
        '''
        print('/' * 30)
        print('Vesti bune, avem {} in cinema-ul nostru!'.format(film.getTitle()))
        print('Titlu: {}\nDescriere: {}\nGen: {}\n'
        .format(film.getTitle(), film.getDescription(), film.getGenre()))
        print('/' * 30)


    @staticmethod
    def show_all_films(filmList):
        '''
        Metoda primeste ca argument lista de filme [Film]
        '''
        print('/' * 30)
        for film in filmList:
            print('Titlu: {}\nDescriere: {}\nGen: {}\n'
            .format(film.getTitle(), film.getDescription(), film.getGenre()))
        print('/' * 30)


    @staticmethod
    def afiseaza_inchirieri(lista):
        print(lista)


    @staticmethod
    def display_missing_film_error(exc):
        print('*' * 20)
        print(str(exc))
        print('*' * 20)

    
    @staticmethod
    def display_film(film):
        print('/' * 30)
        print('Detalii {}:\nId:{}\nDescriere: {}\nGen: {}'
        .format(film.getTitlu(), str(film.getId()), film.getDescriere(), film.getGen()))
        print('/' * 30)

    
    @staticmethod
    def display_missing_client_error(exc):
        print("*" * 20)
        print(str(exc))
        print("*" * 20)


    @staticmethod
    def display_film_deleted_notification():
        print('/' * 30)
        print('Am sters cu succes titlul!')
        print('/' * 30)


    @staticmethod
    def display_film_added(film):
        print('/' * 30)
        print('Am adaugat cu succes {} in colectia noastra!\nDetalii {}:\nId:{}\nDescriere: {}\nGen: {}'
        .format(film.getTitlu(), film.getTitlu(), str(film.getId()), film.getDescriere(), film.getGen()))
        print('/' * 30)


    @staticmethod
    def display_film_updated(film):
        print('/' * 30)
        print('Am modificat cu succes {} in colectia noastra!\nDetalii {}:\nId:{}\nDescriere: {}\nGen: {}'
        .format(film.getTitlu(), film.getTitlu(), str(film.getId()), film.getDescriere(), film.getGen()))
        print('/' * 30)


    @staticmethod
    def display_client_added(client):
        print('/' * 30)
        print('Am adaugat cu succes pe {} in sistemul nostru!\nDetalii:\nId:{}\nNume: {}\nCNP: {}'
        .format(client.getName(), str(client.getId()), client.getName(), str(client.getCnp())))
        print('/' * 30)


    @staticmethod
    def CnpNotValid(err):
        print('*' * 20)
        print('{}'.format(str(err)))
        print('*' * 20)


    @staticmethod
    def FilmAlreadyExists(err):
        print('*' * 20)
        print('{}'.format(str(err)))
        print('*' * 20)


    @staticmethod
    def display_generic_error(err):
        print('*' * 20)
        print('{}'.format(str(err)))
        print('*' * 20)