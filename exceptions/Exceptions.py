class CnpNotNumber(Exception):
    def __init__(self, message = 'CNP-ul trebuie sa contina doar numere!'):
        self.__message = message
        super().__init__(self.__message) # = raise exception mesaj


class CnpNotValid(Exception):
    def __init__(self, message = 'CNP-ul trebuie sa aibe 13 cifre exact!'):
        self.__message = message
        super().__init__(self.__message)


class FilmAlreadyExists(Exception):
    pass


class FilmNotFound(Exception):
    pass