from domain.Client import Client
from domain.InstanceCounter import InstanceCounter
from exceptions.Exceptions import CnpNotNumber, CnpNotValid
class Controller:
    def __init__(self, validare_client, repo):
        self.__validare = validare_client
        self.__repo = repo
        self.__ic = InstanceCounter()


    def adaugare_client(self, nume, cnp):
        client = Client(self.__ic.getNewClientId(), nume, cnp)
        try:
            self.__validare.validare_client(client)
        except CnpNotValid or CnpNotNumber as exc:
            print(str(exc))
            return False
        self.__repo.adauga_client(client)
        return True
        