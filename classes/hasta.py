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
    def tedaviSuresiHesapla(self):
        tedaviSuresi = 0
        # GERİ DÖNÜLECEK!!!!!!
    def __str__(self):
        return "Hasta Bilgileri: ","\nHasta No: ", self.hastaNo, "\nAd: ", self.ad, "\nSoyad: ", self.soyad, "\nDogum Tarihi: ", self.dogumTarihi, "\nHastalik: ", self.hastalik, "\nTedavi: ", self.tedavi


