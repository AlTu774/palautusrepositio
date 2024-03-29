from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from peli import Peli
from pelaaja import Pelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()


        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            #kaksinpeli = KPSPelaajaVsPelaaja()
            #kaksinpeli.pelaa()
            eka_pelaaja = Pelaaja()
            toka_pelaaja = Pelaaja()

        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            eka_pelaaja = Pelaaja()
            toka_pelaaja = Tekoaly()

        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            eka_pelaaja = Pelaaja()
            toka_pelaaja = TekoalyParannettu(10)
        
        else:
            break
        
        peli = Peli(eka_pelaaja, toka_pelaaja)
        peli.pelaa()


if __name__ == "__main__":
    main()
