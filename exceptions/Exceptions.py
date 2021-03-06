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


class ClientNotFound(Exception):
    def __init__(self, message = 'Clientul cautat nu exista!'):
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


class FilmTitleTooShort(Exception):
    def __init__(self, message = 'Titlul filmului trebuie sa fie mai lung de atat!'):
        self.__message = message
        super().__init__(self.__message)


class FilmDescriptionTooShort(Exception):
    def __init__(self, message = 'Descrierea filmului trebuie sa fie mai lunga de atat!'):
        self.__message = message
        super().__init__(self.__message)


class FilmGenreTooShort(Exception):
    def __init__(self, message = 'Genul filmului trebuie sa fie mai lung de atat!'):
        self.__message = message
        super().__init__(self.__message)


class IdIsNotNumber(Exception):
    def __init__(self, message = 'ID-ul oferit nu este numar!'):
        self.__message = message
        super().__init__(self.__message)

    
class FilmDejaInchiriat(Exception):
    def __init__(self, message = 'Filmul acesta este deja inchiriat!'):
        self.__message = message
        super().__init__(self.__message)


class FilmNuEsteInchiriat(Exception):
    def __init__(self, message = 'Filmul acesta nu este inchiriat de acest client!'):
        self.__message = message
        super().__init__(self.__message)