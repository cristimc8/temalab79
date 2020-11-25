from domain.Film import Film
from domain.Client import Client
from domain.Inchirieri import Inchirieri
from domain.InstanceCounter import InstanceCounter
from infrastructure.FilmRepo import FilmRepo
from infrastructure.ClientRepo import ClientRepo
from infrastructure.InchirieriRepo import InchirieriRepo
from controller.FilmService import FilmService
from controller.ClientService import ClientService
from controller.InchirieriService import InchirieriService
from validare.Validare import Validare
class Teste:
    def __init__(self) -> None:
        self.__ic = InstanceCounter()
        self.__valid = Validare()
        self.__clientRepo = ClientRepo()
        self.__filmRepo = FilmRepo()
        self.__inchirieriRepo = InchirieriRepo()
        self.__filmSrv = FilmService(self.__filmRepo, self.__valid)
        self.__clientSrv = ClientService(self.__clientRepo, self.__valid)
        self.__inchirieriSrv = InchirieriService(self.__inchirieriRepo, self.__clientSrv, self.__filmSrv)


    def run_all_tests(self) -> None:
        self.run_teste_film()
        self.run_teste_client()
        self.run_teste_inchirieri()


    def run_teste_film(self) -> None:
        self.test_creaza_film("Titanic", "super tare", "Actiune")
        self.test_get_film_by_id(1)
        self.test_cauta_film_dupa_id(1)
        self.test_get_film_by_title("Titanic")
        self.test_creaza_film("Gigantic", "super tare", "Comedie")
        self.test_modifica_film(2, "Mega", "Descriere", "gen")
        self.test_del_film(2)

    
    def run_teste_client(self) -> None:
        self.test_creaza_client("Vasalie", "1234567891234")
        self.test_get_client_by_id(1)
        self.test_cauta_client_dupa_id(1)
        self.test_get_client_by_name("Vasalie")
        self.test_creaza_client("Geon", "1234567851234")
        self.test_modifica_client(2, "Gion", "1236567851234")
        self.test_del_client(2)

    
    def run_teste_inchirieri(self) -> None:
        self.test_inchiriaza_film(1, 1)
        self.test_get_inchirieri_nereturnate()
        self.test_get_inchirireri_client(1)
        self.test_returnare_inchiriere(1, 1)
        self.test_returneaza_clienti_ordonat_inchirieri()
        self.test_returneaza_cele_mai_inchiriate_filme()
        self.test_get_clienti_ordonat_dupa_filme_inchiriate()
        self.test_primii_30perc_clienti()


    def test_primii_30perc_clienti(self):
        listaOrdonata = self.__inchirieriSrv.get_primii_30perc_clienti()
        assert(listaOrdonata['Vasalie'] == 1)


    def test_returneaza_cele_mai_inchiriate_filme(self):
        listaFilmeOrdonate = self.__inchirieriSrv.get_cele_mai_inchiriate()
        for film in listaFilmeOrdonate.keys():
            assert(listaFilmeOrdonate[film] == 1)


    def test_get_clienti_ordonat_dupa_filme_inchiriate(self):
        listaOrdonata = self.__inchirieriSrv.get_clienti_ordonat_dupa_filme_inchiriate()
        assert (listaOrdonata['Vasalie'] == 1)


    def test_returneaza_clienti_ordonat_inchirieri(self):
        listaOrdonata = self.__inchirieriSrv.get_clients_ordered_by_name()
        assert(listaOrdonata[0].getClient().getName() == 'Vasalie')


    def test_inchiriaza_film(self, idC, idF):
        self.__inchirieriSrv.adaugare_inchiriere(idC, idF)


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
        film = self.__filmSrv.get_film_by_id(id)
        assert(type(film) == Film)
        assert(film.getId() == 1)


    def test_get_film_by_title(self, title) -> None:
        film = self.__filmSrv.get_film_by_title(title)
        assert(type(film) == Film)

    
    def test_get_client_by_id(self, id) -> None:
        client = self.__clientSrv.get_client_by_id(id)
        assert(type(client) == Client)


    def test_get_client_by_name(self, name) -> None:
        client = self.__clientSrv.get_client_by_name(name)
        assert(type(client) == Client)


    def test_del_client(self, id) -> None:
        self.__clientRepo.deleteClientFromList(self.__clientSrv.get_client_by_id(id), False)
        assert(len(self.__clientRepo.get_lista_clienti()) == 1)


    def test_del_film(self, id) -> None:
        self.__filmRepo.deleteFilmFromList(self.__filmSrv.get_film_by_id(id), False)
        assert(len(self.__filmRepo.get_lista_filme()) == 1)


    def test_modifica_film(self, id, titlu, descriere, gen):
        self.__filmSrv.modificare_film(id, titlu, descriere, gen)
        assert(self.__filmSrv.get_film_by_id(id).getTitlu() == titlu)
        assert(self.__filmSrv.get_film_by_id(id).getDescriere() == descriere)
        assert(self.__filmSrv.get_film_by_id(id).getGen() == gen)

    
    def test_modifica_client(self, id, nume, cnp):
        self.__clientSrv.modificare_client(id, nume, cnp)
        assert(self.__clientSrv.get_client_by_id(id).getName() == nume)
        assert(self.__clientSrv.get_client_by_id(id).getCnp() == cnp)


    def test_returnare_inchiriere(self, idC, idF):
        film = self.__filmSrv.get_film_by_id(idF)
        assert(self.__inchirieriSrv.este_inchiriat(film) == True)
        self.__inchirieriSrv.returneaza_inchiriere(idC, idF)
        assert(self.__inchirieriSrv.este_inchiriat(film) == False)


    def test_get_inchirieri_nereturnate(self):
        inchirieri = self.__inchirieriSrv.get_inchirieri_nereturnate()
        for inchiriere in inchirieri:
            assert(inchiriere.isReturnat() == False)


    def test_get_inchirireri_client(self, idC):
        client = self.__clientSrv.get_client_by_id(idC)
        inchirieri = self.__inchirieriSrv.get_inchirieri_client(client)
        for inchiriere in inchirieri:
            assert(inchiriere.getClient() == client)


    def test_cauta_film_dupa_id(self, id):
        film = self.__filmSrv.cautare_dupa_id(id)
        assert(type(film) == Film)

    
    def test_cauta_client_dupa_id(self, id):
        client = self.__clientSrv.cauta_client(id)
        assert(type(client) == Client)
