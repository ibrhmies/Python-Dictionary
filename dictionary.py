yaslar = {"İbrahim":18,"Ahmet":21}
#-> süslü parantezler içinde 2 listeyle yapacağımız işi tek liste halinde yaptık

print(yaslar["İbrahim"])

yaslar ["Mehmet"] = 55
# listemize mehmet ve yaş bilgisi eklendi
print(yaslar)

ogrenciler = {
    100: {
        'ad': 'İbrahim',
        'soyad':'SEVEN',
        'yas"': 18
    }
    }
#liste içinde liste tanımlayabiliriz bu metotla.
sonuc = ogrenciler[100]
sonuc = ogrenciler[100]['ad']
#liste içindeki listeden terim alabiliriz.
print(sonuc)


