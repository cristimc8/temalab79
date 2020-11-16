from domain.Film import Film
from domain.InstanceCounter import InstanceCounter
class Teste:
    def run_all_tests(self):
        self.__run_teste_film()
        #self.__run_teste



    def __run_teste_film(self):
        ic = InstanceCounter()
        id = ic.getNewFilmId()
        titlu = "Titanic"
        descriere = "super tare"
        gen = "Actiune"
        film = Film(id, titlu, descriere, gen)
        assert(film.getId() == id)
        assert(film.getTitlu() == titlu)
        assert(film.getDescriere() == descriere)
        assert(film.getGen() == gen)


    def __run_teste_client(self):
        pass