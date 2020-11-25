class Inchirieri:
    '''
    Clasa care se ocupa de inchirieri
    '''
    def __init__(self, client, film) -> None:
        '''
        Primeste ca parametrii un client si un film
        Seteaza parametru returnat la False initial
        '''
        self.__client = client
        self.__film = film
        self.__returnat = False 


    def returneaza(self):
        '''
        Functia care face ca obiectul sa fie returnat
        '''
        self.__returnat = True


    def isReturnat(self):
        '''
        Functia care ne spune daca obiectul a fost returnat
        '''
        return self.__returnat

    
    def getFilm(self):
        '''
        Functia care ne arata ce film a fost inchiriat
        '''
        return self.__film

    
    def getClient(self):
        '''
        Functia care ne arata ce client a inchiriat
        '''
        return self.__client


    def __str__(self) -> str:
        toReturn = str(self.__client)
        if self.isReturnat():
            toReturn += " a returnat "
        else:
            toReturn += " i inchiriat "
        toReturn += str(self.__film)
        return toReturn


    def __eq__(self, o: object) -> bool:
        if self.getClient() == o.getClient() and self.getFilm() == o.getFilm(): return True
        return False