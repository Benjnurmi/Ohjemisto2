# Luokkahierarkia

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def print_info(self):
        print(f"Julkaisun nimi: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä ):
        self.sivumäärä = sivumäärä
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    def print_info(self):
        super().print_info()
        print(f"Kirja on {self.sivumäärä}-sivuinen")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def print_info(self):
        super().print_info()
        print(f"Lehden päätoimittaja on {self.päätoimittaja}")


julkaisu = Lehti("Aku Ankka", "Aki Hyppää")
julkaisu1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
julkaisu.print_info()
julkaisu1.print_info()









#Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
"""
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettuMatka = kuljettu_matka

    def kiihdyta(


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
"""















# Mallit
"""
from publication import Publication

class Book(Publication):
    def __init__(self, name, page_count):
        self.page_count = page_count
        super().__init__(name)
        ## TODO: add author

    def print_info(self):
        super().print_info()
        print(f"Olen {self.page_count}-sivuinen kirja.")




from publication import Publication


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    #TODO: add print_info()




from magazine import Magazine
from book import Book
pub1 = Magazine("Julkaisu 1", "Pää Toimittaja")
pub2 = Book("julkaisu 2", 220)
pub1.print_info()
pub2.print_info()




class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi: {self.name}")
"""