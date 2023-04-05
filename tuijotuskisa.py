import random

class Olento:
    def __init__(self, nimi, hurraus, rohkeus, katseen_voima):
        self.nimi = nimi
        self.hurraus = hurraus
        self.rohkeus = rohkeus
        self.katseen_voima = katseen_voima

class Peikko(Olento):
    def __init__(self, nimi, hurraus, rohkeus, katseen_voima):
        super().__init__(nimi, hurraus, rohkeus, katseen_voima)

class Sankari(Olento):
    def __init__(self, nimi, hurraus, rohkeus, katseen_voima):
        super().__init__(nimi, hurraus, rohkeus, katseen_voima)

class Vuorenpeikko(Peikko):
    def __init__(self, nimi=None):
        super().__init__(nimi if nimi else self.arvo_nimi(), "Vuorenpeikko hurraa!", self.arvo_rohkeus(), self.arvo_katseen_voima())

    def arvo_nimi(self):
        return "Vuorenpeikko"

    def arvo_rohkeus(self):
        return random.randint(1, 10)

    def arvo_katseen_voima(self):
        return random.randint(1, 10)

class Luolapeikko(Peikko):
    def __init__(self, nimi=None):
        super().__init__(nimi if nimi else self.arvo_nimi(), "Luolapeikko huutaa!", self.arvo_rohkeus(), self.arvo_katseen_voima())

    def arvo_nimi(self):
        return "Luolapeikko"

    def arvo_rohkeus(self):
        return random.randint(1, 5)

    def arvo_katseen_voima(self):
        return random.randint(1, 5)

# Esimerkkikäyttö
peikko1 = Peikko("Peikko1", "Peikko hurraa!", 7, 8)
sankari1 = Sankari("Sankari1", "Sankari huutaa!", 10, 10)
vuorenpeikko1 = Vuorenpeikko()
luolapeikko1 = Luolapeikko()

print(peikko1.nimi, peikko1.hurraus, peikko1.rohkeus, peikko1.katseen_voima)
print(sankari1.nimi, sankari1.hurraus, sankari1.rohkeus, sankari1.katseen_voima)
print(vuorenpeikko1.nimi, vuorenpeikko1.hurraus, vuorenpeikko1.rohkeus, vuorenpeikko1.katseen_voima)
print(luolapeikko1.nimi, luolapeikko1.hurraus, luolapeikko1.rohkeus, luolapeikko1.katseen_voima)
