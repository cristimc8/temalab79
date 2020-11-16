class Film:
    def __init__(self, id_film, titlu, descriere, gen):
        self.__id_film = id_film
        self.__titlu = titlu
        self.__gen = gen
        self.__descriere = descriere


    def __str__(self) -> str:
        return str(self.getTitlu())

    
    def __eq__(self, o: object) -> bool:
        if self.getTitlu() == o.getTitlu(): return True
        return False


    def getId(self) -> int:
        return int(self.__id_film)


    def getTitlu(self) -> str:
        return self.__titlu

    
    def getGen(self) -> str:
        return self.__gen

    
    def getDescriere(self) -> str:
        return self.__descriere


    def updateTitlu(self, newTitle):
        self.__titlu = newTitle
    

    def updateDescriere(self, newDescriere):
        self.__descriere = newDescriere


    def updateGen(self, newGen):
        self.__gen = newGen