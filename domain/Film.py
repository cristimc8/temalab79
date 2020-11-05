class Film:
    def __init__(self, id_film, titlu, descriere, gen):
        self.__id_film = id_film
        self.__titlu = titlu
        self.__gen = gen
        self.__descriere = descriere


    def __str__(self):
        return str(self)
        #####


    def get_id_film(self):
        return self.__id_film


    def get_titlu(self):
        return self.__titlu

    
    def get_gen(self):
        return self.__gen

    
    def get_descriere(self):
        return self.__descriere