from exceptions.Exceptions import CnpNotValid, CnpNotNumber
class Validare:
    def validare_client(self, client):
        cnp = client.getCnp()
        if len(str(cnp)) != 13: raise CnpNotValid
        try:
            nr = int(cnp)
        except ValueError:
            raise CnpNotNumber