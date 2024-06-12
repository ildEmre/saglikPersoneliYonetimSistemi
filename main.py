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
