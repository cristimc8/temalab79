from os import initgroups
from UI.UI import UI
from exceptions.Exceptions import *
class Console:
    def __init__(self, clientService, filmService, inchiriereService):
        self.__user_input = ''
        self.__dict_batch = {'adauga_client': clientService.adaugare_client, 'adauga_film': filmService.adaugare_film,
        'modifica_film': filmService.modificare_film, 'arata_filme': filmService.display_all_films,
        'sterge_film': filmService.sterge_film, 'inchiriaza_film': filmService.inchiriaza_film, 'inchirieri': filmService.afiseaza_inchirieri,
        'out': exit}

        self.__dict_list = {
            '1': clientService.adaugare_client,
            '2': clientService.sterge_client,
            '3': filmService.adaugare_film,
            '4': filmService.modificare_film,
            '5': filmService.display_all_films,
            '6': filmService.sterge_film,
            '7': inchiriereService.adaugare_inchiriere,
            '8': clientService.modificare_client,
            '9': clientService.display_all_clients,
            '10': inchiriereService.arata_inchirieri,
            '11': inchiriereService.returneaza_inchiriere,
            'out': exit
        }


    def show_input_options_batch(self):
        print("adauga_client <nume> <cnp>")
        print("adauga_film <titlu> <descriere> <gen>")
        print("modifica_film <id> <titlu nou> <descriere noua> <gen nou>")
        print("arata_filme")
        print("sterge_film <id>")
        print("inchiriaza_film <numeClient> <numeFilm>")


    def get_user_input(self):
        return input(">>> ")


    def options_valid(self, option):
        if option == 'out': exit()
        try:
            option = int(option)
        except: return False
        return option >= 1 and option <= 10


    def not_empty(self, input):
        return len(str(input)) > 0

    

    def split_arguments(self, inputUser):
        return list(inputUser.split())


    def show_input_options_select(self):
        #Functie care arata optiunile de selectat ale utilizatorului ca select
        print("1 -> Adauga client")
        print("2 -> Sterge client")
        print("3 -> Adauga film")
        print("4 -> Modifica film")
        print("5 -> Arata filme")
        print("6 -> Sterge Film")
        print("7 -> Inchiriaza film")
        print("8 -> Modifica client")
        print("9 -> Arata toti clientii")
        print("10 -> Arata toate inchirieriile")
        print("11 -> Returneaza un film inchiriat")
        print("out -> iesi? :(")


    def choose_menu(self, input):
        input = int(input)
        try:
            if input == 1: self.meniu_adauga_client()
            elif input == 2: self.meniu_sterge_client()
            elif input == 3: self.meniu_adauga_film()
            elif input == 4: self.meniu_modifica_film()
            elif input == 5: self.__dict_list[self.__user_input]()
            elif input == 6: self.meniu_sterge_film()
            elif input == 7: self.meniu_inchiriaza_film()
            elif input == 8: self.meniu_modifica_client()
            elif input == 9: self.__dict_list[self.__user_input]()
            elif input == 10: self.__dict_list[self.__user_input]()
            elif input == 11: self.meniu_returneaza_inchiriere()
        except (CnpNotValid, CnpNotNumber, CnpAlreadyExists) as exc:
            UI.CnpNotValid(exc)
        except FilmNotFound as exc:
            UI.display_missing_film_error(exc)
        except ClientNotFound as exc:
            UI.display_missing_client_error(exc)
        except FilmAlreadyExists as exc:
            UI.FilmAlreadyExists(exc)
        except (FilmTitleTooShort, FilmDescriptionTooShort, FilmGenreTooShort) as exc:
            UI.display_generic_error(exc)
        except IdIsNotNumber as exc:
            UI.display_generic_error(exc)
        except FilmDejaInchiriat as exc:
            UI.display_generic_error(exc)
        except FilmNuEsteInchiriat as exc:
            UI.display_generic_error(exc)


    def meniu_returneaza_inchiriere(self):
        idC = input("ID-ul clientului care vrea sa returneze: ")
        idF = input("ID-ul filmului pe care vrea clientul sa-l returneze: ")
        self.__dict_list[self.__user_input](idC, idF)


    def meniu_inchiriaza_film(self):
        idC = input("ID-ul clientului care vrea sa inchirieze: ")
        idF = input("ID-ul filmului pe care vrea clientul sa il inchirieze: ")
        self.__dict_list[self.__user_input](idC, idF)


    def meniu_modifica_client(self):
        id = input("ID-ul clientului pe care vrei sa il modifici: ")
        nume = input("Nume nou la client: ")
        cnp = input("CNP nou la client: ")
        self.__dict_list[self.__user_input](id, nume, cnp)


    def meniu_sterge_film(self):
        id = input("ID-ul filmului pe care vrei sa il stergi: ")
        self.__dict_list[self.__user_input](id)


    def meniu_modifica_film(self):
        id = input("ID-ul filmului pe care vrei sa il modifici: ")
        titlu = input("Titlu nou: ")
        descriere = input("Descriere noua: ")
        gen = input("Gen nou: ")
        self.__dict_list[self.__user_input](id, titlu, descriere, gen)


    def meniu_adauga_film(self):
        titlu = input("Titlul filmului: ")
        descriere = input("Descrierea filmului: ")
        gen = input("Genul filmului: ")
        self.__dict_list[self.__user_input](titlu, descriere, gen)

    
    def meniu_adauga_client(self):
        nume_client = input("Nume client: ")
        cnp = input("CNP client(13 cifre): ")
        self.__dict_list[self.__user_input](nume_client, cnp)


    def meniu_sterge_client(self):
        id_client = input("ID-ul clientului pe care vrei sa-l stergi: ")
        self.__dict_list[self.__user_input](id_client)
        

    def run(self):
        '''
        Metoda princiapala a consolei; Tine loop-ul in viata
        '''
        self.greet_user()
        self.show_input_options_select()
        while self.__user_input != 'out':
            self.__user_input = self.get_user_input()
            if not self.options_valid(self.__user_input):
                UI.bad_option_selected()
                continue
            self.choose_menu(self.__user_input)


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