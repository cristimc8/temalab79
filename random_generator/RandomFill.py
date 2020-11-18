import random
import string

class RandomFill:
    def __init__(self) -> None:
        self.names = []
        self.cnps = []

        self.filmTitles = []
        self.filmDescriptions = []
        self.filmGenres = []


    def get_random_clients(self, n):
        self.get_random_names(n)
        self.get_random_cnps(n)

    
    def get_random_films(self, n):
        self.get_random_titles(n)
        self.get_random_descriptions(n)
        self.get_random_genres(n)


    def get_random_string(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str.capitalize()


    def get_random_titles(self, n):
        for i in range(0, n):
            self.filmTitles.append(self.get_random_string(7))


    def get_random_descriptions(self, n):
        for i in range(0, n):
            self.filmDescriptions.append(self.get_random_string(24))
        

    def get_random_genres(self, n):
        for i in range(0, n):
            self.filmGenres.append(self.get_random_string(4))


    def get_random_name(self, length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str.capitalize()


    def get_random_names(self, n):
        for i in range(0, n):
            self.names.append(self.get_random_string(8))

    
    def get_random_cnps(self, n):
        for i in range(0, n):
            self.cnps.append(self.get_random_cnp(13))
            

    def get_random_cnp(self, length):
        numbers = string.digits
        result_str = ''.join(random.choice(numbers) for i in range(length))
        return result_str