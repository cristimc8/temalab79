from TestUnit.Teste import Teste
from UI.Console import Console
from infrastructure.FilmRepo import FilmRepo
from infrastructure.ClientRepo import ClientRepo
from validare.Validare import Validare
from controller.Controller import Controller


if __name__ == "__main__":
    teste = Teste()
    teste.run_all_tests()
    clientRepo = ClientRepo()
    filmRepo = FilmRepo()
    valid = Validare()
    controller = Controller(valid, repo)
    console = Console(controller)
    console.run()