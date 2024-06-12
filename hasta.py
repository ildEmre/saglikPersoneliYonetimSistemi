class Hasta():
    def __init__(self, hastaNo, ad, soyad, dogumTarihi, hastalik, tedavi):
        self.hastaNo = hastaNo
        self.ad = ad
        self.soyad = soyad
        self.dogumTarihi = dogumTarihi
        self.hastalik = hastalik
        self.tedavi = tedavi
    def getHastaNo(self):
        return self.hastaNo
    def setHastaNo(self, hastaNo):
        self.hastaNo = hastaNo
    def getAd(self):
        return self.ad
    def setAd(self, ad):
        self.ad = ad
    def getSoyad(self):
        return self.soyad
    def setSoyad(self, soyad):
        self.soyad = soyad
    def getDogumTarihi(self):
        return self.dogumTarihi
    def setDogumTarihi(self, dogumTarihi):
        self.dogumTarihi = dogumTarihi
    def getHastalik(self):
        return self.hastalik
    def setHastalik(self, hastalik):
        self.hastalik = hastalik
    def getTedavi(self):
        return self.tedavi
    def setTedavi(self, tedavi):
        self.tedavi = tedavi
    def tedaviSuresiHesapla(self):
        if self.hastalik == "Grip":
            return 7
        if self.hastalik == "Faranjit":
            return 14
        if self.hastalik == "Fıtık":
            return 100
    def __str__(self):
        return f"Hasta Bilgileri: \nHasta No: {self.hastaNo}\nAd: {self.ad}\nSoyad: {self.soyad}\nDogum Tarihi: {self.dogumTarihi}\nHastalik: {self.hastalik}\nTedavi: {self.tedavi}"


