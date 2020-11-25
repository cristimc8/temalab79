class InstanceCounter:
    '''
    Clasa care numara instantele obiectelor de tip
    :Film
    :Client
    '''
    def __init__(self):
        self.__film = 0
        self.__client = 0


    def getNewFilmId(self):
        #Functie care returneaza un nou id pentru film
        #Date de intrare: -
        #Date de iesire: id Int
        return int(self.__film + 1)

    
    def getNewClientId(self):
        #Functie care returneaza un nou id pentru client
        #Date de intrare: -
        #Date de iesire: id Int
        return int(self.__client + 1)

    
    def updateLastFilmId(self):
        #Functie care actualizeaza ultimul ID pentru film
        self.__film += 1

    
    def updateLastClientId(self):
        #Functie care actualizeaza ultimul ID pentru client
        self.__client += 1

    
    def popClientId(self):
        self.__client -= 1


    def popFilmId(self):
        self.__film -= 1