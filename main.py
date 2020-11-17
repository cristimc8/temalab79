from TestUnit.Teste import Teste
from UI.Console import Console
from infrastructure.FilmRepo import FilmRepo
from infrastructure.ClientRepo import ClientRepo
from validare.Validare import Validare
from controller.ClientService import ClientService
from controller.FilmService import FilmService


if __name__ == "__main__":
    teste = Teste()
    teste.run_all_tests()
    clientRepo = ClientRepo()
    filmRepo = FilmRepo()
    valid = Validare()
    clientService = ClientService(clientRepo, valid)
    filmService = FilmService(filmRepo, valid)
    console = Console(clientService, filmService)
    console.run()
    
    #IN CONSOLE SCHIMBA METODA DE BATCH
    #Sa ma gindesc la ceva cu inchirieri -- relatii antre obiecte
    #Documentatie si scenarii de rulare