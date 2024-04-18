# makas taş kağıt
# list = liste = birden fazla değeri aynı değişkende tutmak için kullanılan bir tür

import random
secim = ["tas","kagıt","makas"]

bilgisayar_hamlesi=random.choice(secim)

kullanici_hamlesi =input("""
        tas, kagit, makas;
        hamlenizi giriniz: 
                               """)

print(f"""
      Bilgisayar hamlesi = {bilgisayar_hamlesi}
      Kullanıcı Hamlesi = {kullanici_hamlesi}""")

if bilgisayar_hamlesi == kullanici_hamlesi :
    print("Berabere!!!")

if bilgisayar_hamlesi == "makas":
    if kullanici_hamlesi == "kagıt":
        print("Kullanıcı kesildi")
    if kullanici_hamlesi == "tas":
        print("bilgisayar kırıldı")

if bilgisayar_hamlesi== "tas": 
    if kullanici_hamlesi == "kagıt":
        print("bilgisayar buruştu")
    if kullanici_hamlesi == "makas" :
        print("kullanıcı kırıldı") 

if bilgisayar_hamlesi== "kagıt": 
    if kullanici_hamlesi == "tas":
      print("kullanıcı buruştu")
    if kullanici_hamlesi == "makas" :
        print("kullanıcı kesildi") 

