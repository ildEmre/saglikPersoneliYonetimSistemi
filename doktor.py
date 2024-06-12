from personel import *
class Doktor(Personel):
    def __init__(self, personelNo, ad, soyad, departman, maas, uzmanlik, deneyimYili, hastane):
        super().__init__(personelNo, ad, soyad, departman, maas)
        self.uzmanlik = uzmanlik
        self.deneyimYili = deneyimYili
        self.hastane = hastane
    def getUzmanlik(self):
        return self.uzmanlik
    def setUzmanlik(self, uzmanlik):
        self.uzmanlik = uzmanlik
    def getDeneyimYili(self):
        return self.deneyimYili
    def setDeneyimYili(self, deneyimYili):
        self.deneyimYili = deneyimYili
    def getHastane(self):
        return self.hastane
    def setHastane(self, hastane):
        self.hastane = hastane
    def __str__(self):
        return super().__str__() + f"\nUzmanlik: {self.uzmanlik}\nDeneyim yili: {self.deneyimYili}\nHastane: {self.hastane}"
    def maasArttir(self):
        self.maas += self.maas * 10/100
