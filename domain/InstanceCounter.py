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
        self.__film += 1
        return int(self.__film)

    
    def getNewClientId(self):
        self.__client += 1
        return int(self.__client)