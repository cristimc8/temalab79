from controller.Controller import Controller


class UI:
    def __init__(self, controller):
        self.__user_input = ''
        self.__dict = {'adauga_client': controller.adaugare_client,
        'out': exit}


    def get_user_input(self):
        return input(">>> ")
    

    def split_arguments(self, inputUser):
        return list(inputUser.split())


    def run(self):
        self.greet_user()
        while self.__user_input != 'out':
            self.__user_input = self.get_user_input()
            args = self.split_arguments(self.__user_input)
            if len(args) == 0:
                continue
            self.parseNumbers(args)
            if args[0] in self.__dict:
                try:
                    self.__dict[args[0]](*args[1:])
                except TypeError:
                    print('Insuficiente argumente!')
            else: print('Comanda inexistenta!')


    @staticmethod
    def greet_user():
        print('/' * 30)
        print('Buna siua, bine ati venit la inchriere filme!')
        print('/' * 30)


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
    def display_missing_film_error(film, err):
        print('*' * 20)
        print('Ne pare rau, dar nu avem {} in colectie!'
        .format(film.getTitle()))
        print('*' * 20)


    @staticmethod
    def display_film_added(film):
        print('/' * 30)
        print('Am adaugat cu succes {} in colectia noastra!'
        .format(film.getTitle()))
        print('/' * 30)


    def parseNumbers(self, lista):
        for index, element in enumerate(lista):
            try:
                element = int(element)
                lista[index] = element
            except ValueError:
                try:
                    element = float(element)
                    lista[index] = element
                except:
                    pass