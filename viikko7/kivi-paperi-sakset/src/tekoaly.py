class Tekoaly:
    def __init__(self):
        self._siirto = 0
        self.siirto_arvo = {0:"k", 1:"p", 2:"s"}

    def tee_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        print(self._siirto, "siirtoooo")
        print(self.siirto_arvo[self._siirto])
        return self.siirto_arvo[self._siirto]
        """else:
            print("s")
            return "s"""

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
