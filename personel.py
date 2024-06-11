class Personel: 
    def __init__(self, personelNo, ad, soyad, departman, maas): #Personel constructor
        self.personelNo = personelNo
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas
    def getNo(self):
        return self.personelNo
    def setNo(self, personelNo):
        self.personelNo = personelNo
    def getAd(self):
        return self.ad
    def setAd(self, ad):
        self.ad = ad
    def getSoyad(self):
        return self.soyad
    def setSoyad(self, soyad):
        self.soyad = soyad
    def getDepartman(self):
        return self.departman
    def setDepartman(self, departman):
        self.departman = departman
    def getMaas(self):
        return self.maas
    def setMaas(self, maas):
        self.maas = maas
    def __str__(self):
        return "Personel Bilgileri: \nAd: ", self.ad, "\nSoyad: ", self.soyad, "\nDepartman: " , self.departman, "\nMaas:", self.maas
    