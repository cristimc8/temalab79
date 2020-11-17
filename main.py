from TestUnit.Teste import Teste
from UI.Console import Console
from infrastructure.Repo import Repo
from validare.Validare import Validare
from controller.Controller import Controller


if __name__ == "__main__":
    teste = Teste()
    teste.run_all_tests()
    repo = Repo()
    valid = Validare()
    controller = Controller(valid, repo)
    console = Console(controller)
    console.run()