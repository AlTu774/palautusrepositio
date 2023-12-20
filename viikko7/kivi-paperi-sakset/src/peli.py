from tuomari import Tuomari

class Peli:
    def __init__(self, pelaaja1, pelaaja2):
        self.tuomari = Tuomari()
        self.pelaaja1 = pelaaja1
        self.pelaaja2 = pelaaja2

    def pelaa(self):
        print("Ensimmäisen pelaajan siirto: ")
        ekan_siirto = self.pelaaja1.tee_siirto()
        print("Toisen pelaajan siirto: ")
        tokan_siirto = self.pelaaja2.tee_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            print("Ensimmäisen pelaajan siirto: ")
            ekan_siirto = self.pelaaja1.tee_siirto()
            print("Toisen pelaajan siirto: ")
            tokan_siirto = self.pelaaja2.tee_siirto()

        print("Kiitos!")
        print(self.tuomari)
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"