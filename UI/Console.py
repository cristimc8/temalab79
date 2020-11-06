class Console:
    def __init__(self, controller):
        self.__user_input = ''
        self.__dict = {'adauga_client': controller.adaugare_client, 'adauga_film': controller.adaugare_film,
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
                except TypeError as exc:
                    print('Insuficiente argumente!' + str(exc))
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