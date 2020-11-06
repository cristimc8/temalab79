class CnpNotNumber(Exception):
    def __init__(self, message = 'CNP-ul trebuie sa contina doar numere!'):
        self.__message = message
        super().__init__(self.__message) # = raise exception mesaj


class CnpNotValid(Exception):
    def __init__(self, message = 'CNP-ul trebuie sa aibe 13 cifre exact!'):
        self.__message = message
        super().__init__(self.__message)


class CnpAlreadyExists(Exception):
    def __init__(self, message = 'CNP-ul este deja inregistrat!'):
        self.__message = message
        super().__init__(self.__message)


class FilmAlreadyExists(Exception):
    def __init__(self, message = 'Filmul acesta exista deja!'):
        self.__message = message
        super().__init__(self.__message)


class FilmNotFound(Exception):
    def __init__(self, message = 'Filmul cautat nu exista inca!'):
        self.__message = message
        super().__init__(self.__message)