from exceptions.Exceptions import *
class Validare:
    def validare_client(self, client):
        cnp = client.getCnp()
        if len(str(cnp)) != 13: raise CnpNotValid
        try:
            nr = int(cnp)
        except ValueError:
            raise CnpNotNumber
        #if client in listaClienti:
        #    raise CnpAlreadyExists

    
    def validare_film(self, film):
        if len(film.getTitlu()) == 0:
            raise FilmTitleTooShort
        if len(film.getDescriere()) == 0:
            raise FilmDescriptionTooShort
        if len(film.getGen()) == 0:
            raise FilmGenreTooShort
        #if film in listaFilme:
        #    raise FilmAlreadyExists