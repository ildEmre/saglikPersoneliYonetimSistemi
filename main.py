try:
    from classes import personel, hasta, hemsire, doktor
except:
    print("Dosya yüklenirken hata oluştu. Tekrar deneyiniz.")
try:
    from pandas import DataFrame, Series
except:
    print("Dosya yüklenirken hata oluştu. Tekrar deneyiniz.")

data = DataFrame({ 
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
personel1 = personel(104, "Emre", "İldeniz", "Kardiyoloji", 45000)
personel2 = personel(105, "Furkan", "Yılmaz", "Radyoloji", 50000)
doktor1 = doktor(110, "Murat", "Demir", "Nöroloji", 55000, "Nörolog", 3, "Hastane1")
doktor2 = doktor(111, "Talha", "Aydın", "Üroloji", 60000, "Ürolog", 4, "Hastane2")
doktor3 = doktor(112, "Zeynep", "Dağ", "Onkoloji", 60000, "Onkolog" 5, "Hastane3" )
hemsire1 = hemsire(120, "Betül", "Aydın","Radyoloji", 40000, 12, "Radyoloji Sertifikası", "Hastane1")
hemsire2 = hemsire(121, "Faruk", "Yavuz","Anestezi", 45000, 10, "Anestezi Sertifikası", "Hastane2")
hemsire3 = hemsire(122, "Orkun", "Yılmaz","Cerrahi", 40000, 14, "Cerrahi Sertifikası", "Hastane3")
hasta1 = hasta(10, "Mert", "İldeniz", 2000, "Grip", "İlaç")
hasta2 = hasta(11, "Yaren", "Demir", 2002, "Faranjit", "İlaç")
hasta3 = hasta(12, "Adil", "Polat", 1980, "Fıtık", "Ameliyat")

personelList = [
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
        "Uzmanlık":    doktor1.getUzmanlik(),
        "Deneyim Yılı": doktor1.getDeneyimYili(),
        "Hastane": doktor1.getHastane()
    }),

    Series({
        "Personel No":  doktor2.getNo(),
        "Ad":           doktor2.getAd(),
        "Soyad":        doktor2.getSoyad(),
        "Departman":    doktor2.getDepartman(),
        "Maas":         doktor2.getMaas(),
        "Uzmanlık":    doktor2.getUzmanlik(),
        "Deneyim Yılı": doktor2.getDeneyimYili(),
        "Hastane": doktor2.getHastane()
    }),

    Series({
        "Personel No":  doktor3.getNo(),
        "Ad":           doktor3.getAd(),
        "Soyad":        doktor3.getSoyad(),
        "Departman":    doktor3.getDepartman(),
        "Maas":         doktor3.getMaas(),
        "Uzmanlık":    doktor3.getUzmanlik(),
        "Deneyim Yılı": doktor3.getDeneyimYili(),
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
        "Çalışma Saati": hemsire1.getSaat(),
        "Sertifika": hemsire1.getSertifika(),
        "Hastane": hemsire1.getHastane()
    })

    Series({
        "Personel No":  hemsire2.getNo(),
        "Ad":           hemsire2.getAd(),
        "Soyad":        hemsire2.getSoyad(),
        "Departman":    hemsire2.getDepartman(),
        "Maas":         hemsire2.getMaas(),
        "Çalışma Saati": hemsire2.getSaat(),
        "Sertifika": hemsire2.getSertifika(),
        "Hastane": hemsire2.getHastane()
    })

    Series({
        "Personel No":  hemsire3.getNo(),
        "Ad":           hemsire3.getAd(),
        "Soyad":        hemsire3.getSoyad(),
        "Departman":    hemsire3.getDepartman(),
        "Maas":         hemsire3.getMaas(),
        "Çalışma Saati": hemsire3.getSaat(),
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
        "Hastalık": hasta1.getHastalik(),
        "Tedavi": hasta1.getTedavi()
    })

    Series({
        "Hasta No": hasta2.getHastaNo(),
        "Ad": hasta2.getAd(),
        "Soyad": hasta2.getSoyad(),
        "Doğum Tarihi": hasta2.getDogumTarihi(),
        "Hastalık": hasta2.getHastalik(),
        "Tedavi": hasta2.getTedavi()
    })

    Series({
        "Hasta No": hasta3.getHastaNo(),
        "Ad": hasta3.getAd(),
        "Soyad": hasta3.getSoyad(),
        "Doğum Tarihi": hasta3.getDogumTarihi(),
        "Hastalık": hasta3.getHastalik(),
        "Tedavi": hasta3.getTedavi()
    })
]

for personel in personelList:
    data.loc[len(data)] = personel  #Series i dataframe'e ekleme işlemi

for doktor in doktorList:
    data.loc[len(data)] = doktor

for hemsire in hemsireList:
    data.loc[len(data)] = hemsire

for hasta in hastaList:
    data.loc[len(data)] = hasta

data = data.fillna(0)
newData = data.get(["Ad", "Soyad", "Departman", "Maas", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi"])