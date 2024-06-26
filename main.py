try:
    from personel import Personel
    from doktor import Doktor
    from hasta import Hasta
    from hemsire import Hemsire
except ImportError:
    print("Dosya yüklenirken hata oluştu. Tekrar deneyiniz.")
    raise
try:
    from pandas import DataFrame, Series
except ImportError:
    print("Dosya yüklenirken hata oluştu. Tekrar deneyiniz.")
    raise

data = DataFrame({ #Tüm instance lar kullanılarak oluşturulan ana dataframe
    "Personel No":  [],
    "Ad":           [],
    "Soyad":        [],
    "Departman":    [],
    "Maas":         [],
    "Uzmanlik":     [],
    "Deneyim Yili": [],
    "Hastane":      [],
    "Calisma Saati":[],
    "Sertifika":    [],
    "Hasta No" :    [],
    "Dogum Tarihi" :[],
    "Hastalik" :    [],
    "Tedavi" :      []
})
personel1 = Personel(104, "Emre", "İldeniz", "Kardiyoloji", 45000)
print(str(personel1))
personel2 = Personel(105, "Furkan", "Yılmaz", "Radyoloji", 50000)
print(str(personel2))
doktor1 = Doktor(110, "Murat", "Demir", "Nöroloji", 55000, "Nörolog", 3, "Alsancak Devlet Hastanesi")
print(str(doktor1))
doktor2 = Doktor(111, "Talha", "Aydın", "Üroloji", 60000, "Ürolog", 4, "Karşıyaka Devlet Hastanesi")
print(str(doktor2))
doktor3 = Doktor(112, "Zeynep", "Dağ", "Onkoloji", 60000, "Onkolog", 6, "Çiğli Eğitim ve Araştırma Hastanesi" )
print(str(doktor3))
hemsire1 = Hemsire(120, "Betül", "Aydın","Radyoloji", 40000, 12, "Radyoloji Sertifikası", "Alsancak Devlet Hastanesi")
print(str(hemsire1))
hemsire2 = Hemsire(121, "Faruk", "Yavuz","Anestezi", 45000, 10, "Anestezi Sertifikası", "Karşıyaka Devlet Hastanesi")
print(str(hemsire2))
hemsire3 = Hemsire(122, "Orkun", "Yılmaz","Genel Cerrahi", 40000, 14, "Cerrahi Sertifikası", "Çiğli Eğitim ve Araştırma Hastanesi")
print(str(hemsire3))
hasta1 = Hasta(10, "Mert", "İldeniz", 2000, "Grip", "İlaç")
print(str(hasta1))
hasta2 = Hasta(11, "Yaren", "Demir", 1990, "Faranjit", "İlaç")
print(str(hasta2))
hasta3 = Hasta(12, "Adil", "Polat", 1970, "Fıtık", "Ameliyat")
print(str(hasta3))

personelList = [ #Dataframe'e eklenmek için oluşturulan Series objectleri
    Series({
        "Personel No":  personel1.getNo(),
        "Ad":           personel1.getAd(),
        "Soyad":        personel1.getSoyad(),
        "Departman":    personel1.getDepartman(),
        "Maas":         personel1.getMaas()
    }),

    Series({
        "Personel No":  personel2.getNo(),
        "Ad":           personel2.getAd(),
        "Soyad":        personel2.getSoyad(),
        "Departman":    personel2.getDepartman(),
        "Maas":         personel2.getMaas()
    }),
]

doktorList = [
    Series({
        "Personel No":  doktor1.getNo(),
        "Ad":           doktor1.getAd(),
        "Soyad":        doktor1.getSoyad(),
        "Departman":    doktor1.getDepartman(),
        "Maas":         doktor1.getMaas(),
        "Uzmanlik":    doktor1.getUzmanlik(),
        "Deneyim Yili": doktor1.getDeneyimYili(),
        "Hastane": doktor1.getHastane()
    }),

    Series({
        "Personel No":  doktor2.getNo(),
        "Ad":           doktor2.getAd(),
        "Soyad":        doktor2.getSoyad(),
        "Departman":    doktor2.getDepartman(),
        "Maas":         doktor2.getMaas(),
        "Uzmanlik":    doktor2.getUzmanlik(),
        "Deneyim Yili": doktor2.getDeneyimYili(),
        "Hastane": doktor2.getHastane()
    }),

    Series({
        "Personel No":  doktor3.getNo(),
        "Ad":           doktor3.getAd(),
        "Soyad":        doktor3.getSoyad(),
        "Departman":    doktor3.getDepartman(),
        "Maas":         doktor3.getMaas(),
        "Uzmanlik":    doktor3.getUzmanlik(),
        "Deneyim Yili": doktor3.getDeneyimYili(),
        "Hastane": doktor3.getHastane()
    })
]

hemsireList = [
    Series({
        "Personel No":  hemsire1.getNo(),
        "Ad":           hemsire1.getAd(),
        "Soyad":        hemsire1.getSoyad(),
        "Departman":    hemsire1.getDepartman(),
        "Maas":         hemsire1.getMaas(),
        "Calisma Saati": hemsire1.getSaat(),
        "Sertifika": hemsire1.getSertifika(),
        "Hastane": hemsire1.getHastane()
    }),

    Series({
        "Personel No":  hemsire2.getNo(),
        "Ad":           hemsire2.getAd(),
        "Soyad":        hemsire2.getSoyad(),
        "Departman":    hemsire2.getDepartman(),
        "Maas":         hemsire2.getMaas(),
        "Calisma Saati": hemsire2.getSaat(),
        "Sertifika": hemsire2.getSertifika(),
        "Hastane": hemsire2.getHastane()
    }),

    Series({
        "Personel No":  hemsire3.getNo(),
        "Ad":           hemsire3.getAd(),
        "Soyad":        hemsire3.getSoyad(),
        "Departman":    hemsire3.getDepartman(),
        "Maas":         hemsire3.getMaas(),
        "Calisma Saati": hemsire3.getSaat(),
        "Sertifika": hemsire3.getSertifika(),
        "Hastane": hemsire3.getHastane()
    })
]

hastaList = [

    Series({
        "Hasta No": hasta1.getHastaNo(),
        "Ad": hasta1.getAd(),
        "Soyad": hasta1.getSoyad(),
        "Doğum Tarihi": hasta1.getDogumTarihi(),
        "Hastalik": hasta1.getHastalik(),
        "Tedavi": hasta1.getTedavi()
    }),

    Series({
        "Hasta No": hasta2.getHastaNo(),
        "Ad": hasta2.getAd(),
        "Soyad": hasta2.getSoyad(),
        "Doğum Tarihi": hasta2.getDogumTarihi(),
        "Hastalik": hasta2.getHastalik(),
        "Tedavi": hasta2.getTedavi()
    }),

    Series({
        "Hasta No": hasta3.getHastaNo(),
        "Ad": hasta3.getAd(),
        "Soyad": hasta3.getSoyad(),
        "Doğum Tarihi": hasta3.getDogumTarihi(),
        "Hastalik": hasta3.getHastalik(),
        "Tedavi": hasta3.getTedavi()
    })
]

for personel in personelList:  #personelList listesi içinde dönerek tüm personel rowlarını okuyup data dataframeine ekleyen bir loop
    data.loc[len(data)] = personel  
            # data'nın uzunluğunu endeks alan rowa erişmeyi sağlayan .loc metodu
for doktor in doktorList:
    data.loc[len(data)] = doktor #İşlem tekrar edilir

for hemsire in hemsireList:
    data.loc[len(data)] = hemsire

for hasta in hastaList: #Hasta rowlarında farklı instancelar olduğundan sadece kendi instancelarını okuttum
    data.loc[len(data)] = {
        "Hasta No": hasta["Hasta No"],
        "Ad": hasta["Ad"],
        "Soyad": hasta["Soyad"],
        "Dogum Tarihi": hasta["Doğum Tarihi"],
        "Hastalik": hasta["Hastalik"],
        "Tedavi": hasta["Tedavi"]
    }

data = data.fillna(0) #NaN olan instancelara 0 atanma işlemi


doktorSayi = data[data["Uzmanlik"] != 0].groupby("Uzmanlik").size() # 0 olmayan uzmanlik instancelarına göre gruplama işlemi
#Doktorları Uzmanlık alanına göre gruplama işlemi
print("Doktor Sayısı Uzmanlık Alanına Göre:")
print(doktorSayi)
print("................................................................................................................................")

#Maas instanceının 7000 den büyük olduğu rowları bulma ve sonrasında bu rowların hepsini yuksekMaas dataframeinde saklayıp yazdırma işlemi
yuksekMaas = data[data["Maas"]>7000]
print("Maaşı 7000'den fazla olan personeller: ")
print(yuksekMaas)
print("................................................................................................................................")

#Deneyim Yili instanceının 5 den büyük ve uzmanlığın 0 olmadığı(doktor olan)
#rowların sayısını hesaplayıp deneyimli dataframeinde sakladıktan sonra yazdırma işlemi
deneyimli = data[(data["Deneyim Yili"] > 5) & (data["Uzmanlik"] != 0)].shape[0]
print("5 Yıldan fazla deneyime sahip doktor sayısı: ")
print(deneyimli)
print("................................................................................................................................")

hastaAdi = data[data["Hasta No"] != 0] #Hasta Nosu 0 olmayan rowları yani hastaları bulup hastaAdi dataframeinde saklama işlemi
print("Alfabetik olarak sıralanmış şekilde hastalar: ")
print(hastaAdi.sort_values("Ad")) #Ad instanceına göre A'dan Z'ye olacak şekilde rowları sıralayıp yazdırma işlemi
print("................................................................................................................................")

dogumHasta = data[(data["Hasta No"] !=0 ) & (data["Dogum Tarihi"] >= 1990)] #Tekrar hasta no instanceından hasta rowları bulunup 
                                                                            #dogum tarihi instanceı 1990 ve sonrası olan hastalar bulunup yazdırılıyor
print("1990 yılı ve sonrasında doğmuş hastalar: ")
print(dogumHasta)
print("................................................................................................................................")
print("Tüm DataFrame: ")
newData = data[["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastalik", "Tedavi"]]
print(newData)