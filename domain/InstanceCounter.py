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
        return int(self.__film + 1)

    
    def getNewClientId(self):
        return int(self.__client + 1)

    
    def updateLastFilmId(self):
        self.__film += 1

    
    def updateLastClientId(self):
        self.__client += 1

    
    def popClientId(self):
        self.__client -= 1


    def popFilmId(self):
        self.__film -= 1