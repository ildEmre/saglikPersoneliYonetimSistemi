from personel import *
class Hemsire(Personel):
    def __init__(self, personelNo, ad, soyad, departman, maas, calismaSaati, sertifika, hastane):
        super().__init__(personelNo, ad, soyad, departman, maas)
        self.calismaSaati = calismaSaati
        self.sertifika = sertifika
        self.hastane = hastane
    def getSaat(self):
        return self.calismaSaati
    def setSaat(self, calismaSaati):
        self.calismaSaati = calismaSaati
    def getSertifika(self):
        return self.sertifika
    def setSertifika(self, sertifika):
        self.sertifika = sertifika
    def getHastane(self):
        return self.hastane
    def setHastane(self, hastane):
        self.hastane = hastane
    def __str__(self):
        return super().__str__() + "\nCalisma Saati: ", self.calismaSaati, "\nSertifika: ", self.sertifika, "\nHastane: ", self.hastane
    def maasArttir(self, oran):
        self.maas += self.maas * oran/100