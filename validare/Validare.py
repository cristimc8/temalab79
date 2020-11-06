from exceptions.Exceptions import *
class Validare:
    def validare_client(self, client, listaClienti):
        cnp = client.getCnp()
        if len(str(cnp)) != 13: raise CnpNotValid
        try:
            nr = int(cnp)
        except ValueError:
            raise CnpNotNumber
        if client in listaClienti:
            raise CnpAlreadyExists

    
    def validare_film(self, film, listaFilme):
        if film in listaFilme:
            raise FilmAlreadyExists