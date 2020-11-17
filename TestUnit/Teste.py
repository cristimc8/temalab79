from domain.Film import Film
from domain.Client import Client
from domain.InstanceCounter import InstanceCounter
from infrastructure.FilmRepo import FilmRepo
from infrastructure.ClientRepo import ClientRepo
class Teste:
    def __init__(self) -> None:
        self.__ic = InstanceCounter()
        self.__clientRepo = ClientRepo()
        self.__filmRepo = FilmRepo()


    def run_all_tests(self) -> None:
        self.run_teste_film()
        self.run_teste_client()


    def run_teste_film(self) -> None:
        self.test_creaza_film("Titanic", "super tare", "Actiune")
        self.test_get_film_by_id(1)
        self.test_get_film_by_title("Titanic")
        self.test_del_film(1)

    
    def run_teste_client(self) -> None:
        self.test_creaza_client("Vasalie", "1234567891234")
        self.test_get_client_by_id(1)
        self.test_get_client_by_name("Vasalie")


    def test_creaza_film(self, titlu, descriere, gen) -> None:
        id = self.__ic.getNewFilmId()
        film = Film(id, titlu, descriere, gen)
        assert(film.getId() == id)
        assert(film.getTitlu() == titlu)
        assert(film.getDescriere() == descriere)
        assert(film.getGen() == gen)
        self.__ic.updateLastFilmId()
        self.__filmRepo.adauga_film(film, False)


    def test_creaza_client(self, nume, cnp) -> None:
        id = self.__ic.getNewClientId()
        client = Client(id, nume, cnp)
        assert(client.getId() == id)
        assert(client.getName() == nume)
        assert(client.getCnp() == cnp)
        self.__ic.updateLastClientId()
        self.__clientRepo.adauga_client(client, False)


    def test_get_film_by_id(self, id) -> None:
        film = self.__filmRepo.get_film_by_id(id)
        assert(type(film) == Film)


    def test_get_film_by_title(self, title) -> None:
        film = self.__filmRepo.get_film_by_title(title)
        assert(type(film) == Film)

    
    def test_get_client_by_id(self, id) -> None:
        client = self.__clientRepo.get_client_by_id(id)
        assert(type(client) == Client)


    def test_get_client_by_name(self, name) -> None:
        client = self.__clientRepo.get_client_by_name(name)
        assert(type(client) == Client)


    def test_del_client(self, id) -> None:
        self.__clientRepo.deleteClientFromList(self.__clientRepo.get_client_by_id(id), False)


    def test_del_film(self, id) -> None:
        self.__filmRepo.deleteFilmFromList(self.__filmRepo.get_film_by_id(id), False)