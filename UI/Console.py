from UI.UI import UI
from exceptions.Exceptions import *
class Console:
    def __init__(self, controller):
        self.__user_input = ''
        self.__dict = {'adauga_client': controller.adaugare_client, 'adauga_film': controller.adaugare_film,
        'modifica_film': controller.modificare_film, 'arata_filme': controller.display_all_films,
        'sterge_film': controller.sterge_film, 'inchiriaza_film': controller.inchiriaza_film, 'inchirieri': controller.afiseaza_inchirieri,
        'out': exit}


    def show_input_options(self):
        print("adauga_client <nume> <cnp>")
        print("adauga_film <titlu> <descriere> <gen>")
        print("modifica_film <id> <titlu nou> <descriere noua> <gen nou>")
        print("arata_filme")
        print("sterge_film <id>")
        print("inchiriaza_film <numeClient> <numeFilm>")


    def get_user_input(self):
        return input(">>> ")

    

    def split_arguments(self, inputUser):
        return list(inputUser.split())


    def run(self):
        self.greet_user()
        self.show_input_options()
        while self.__user_input != 'out':
            self.__user_input = self.get_user_input()
            args = self.split_arguments(self.__user_input)
            if len(args) == 0:
                continue
            self.parseNumbers(args)
            if args[0] in self.__dict:
                try:
                    self.__dict[args[0]](*args[1:])
                except TypeError as exc:
                    print('Insuficiente argumente!' + str(exc))
                except (CnpNotValid, CnpNotNumber, CnpAlreadyExists) as exc:
                    UI.CnpNotValid(exc)
                except FilmNotFound as exc:
                    UI.display_missing_film_error(exc)
                except ClientNotFound as exc:
                    UI.display_missing_client_error(exc)
            else: print('Comanda inexistenta!')


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


    def greet_user(self):
        print('/' * 30)
        print('Buna siua, bine ati venit la inchiriere filme!')
        print('/' * 30)