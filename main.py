from TestUnit.Teste import Teste
from UI.Console import Console
from infrastructure.FilmRepo import FilmRepo
from infrastructure.ClientRepo import ClientRepo
from infrastructure.InchirieriRepo import InchirieriRepo
from validare.Validare import Validare
from controller.ClientService import ClientService
from controller.FilmService import FilmService
from controller.InchirieriService import InchirieriService


if __name__ == "__main__":
    teste = Teste()
    teste.run_all_tests()
    clientRepo = ClientRepo()
    filmRepo = FilmRepo()
    inchirieriRepo = InchirieriRepo()
    valid = Validare()
    clientService = ClientService(clientRepo, valid)
    filmService = FilmService(filmRepo, valid)
    inchirieriService = InchirieriService(inchirieriRepo, clientService, filmService)
    console = Console(clientService, filmService, inchirieriService)
    console.run()