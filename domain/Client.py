class Client:
    '''
    Clasa pentru crearea obiectului 'Client'
    Clasa contine: id, nume, CNP
    '''
    def __init__(self, id, name, cnp):
        '''
        Clasa care initializeaza obiectul Film cu parametrii
        :id: Int
        :nume: String
        :cnp: String
        '''
        self.__id = id
        self.__name = name
        self.__cnp = cnp


    def __str__(self) -> str:
        return str(self.__name)


    def __eq__(self, o: object) -> bool:
        if self.getCnp() == o.getCnp(): return True
        return False


    def getId(self):
        '''
        Functie care returneaza id-ul clientului
        :out: id Int
        '''
        return int(self.__id)

    
    def getName(self):
        '''
        Functie care returneaza numele Clientului
        :out: nume String
        '''
        return self.__name
    

    def getCnp(self):
        '''
        Functie care returneaza cnp-ul Clientului
        :out: cnp String
        '''
        return self.__cnp