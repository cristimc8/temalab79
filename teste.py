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
        assert(film.get_id_film() == id)
        assert(film.get_titlu() == titlu)
        assert(film.get_descriere() == descriere)
        assert(film.get_gen() == gen)