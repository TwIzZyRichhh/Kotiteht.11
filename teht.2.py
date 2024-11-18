class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        if nopeus <= self.huippunopeus:
            self.nopeus = nopeus
        else:
            self.nopeus = self.huippunopeus

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

def main():
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    sahkoauto.aseta_nopeus(120)
    polttomoottoriauto.aseta_nopeus(150)
    sahkoauto.aja(3)
    polttomoottoriauto.aja(3)

    print(f"Sähköauton ({sahkoauto.rekisteritunnus}) matkamittarilukema: {sahkoauto.matkamittari} km")
    print(f"Polttomoottoriauton ({polttomoottoriauto.rekisteritunnus}) matkamittarilukema: {polttomoottoriauto.matkamittari} km")

if __name__ == "__main__":
    main()
