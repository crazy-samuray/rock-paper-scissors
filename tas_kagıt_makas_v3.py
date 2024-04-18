import random

secim = ["TAŞ","KAĞIT","MAKAS"]

bilgisayar_puan=0
kullanici_puan=0


bilgisayar_hamlesi = random.choice(secim)

kullanici_hamlesi = input("""
                         Bu oyunda bilgisayar ve ya oyuncu 3 puan alırsa kazanır ve oyun biter;
                         TAŞ, KAĞIT, MAKAS;        hamlenizi giriniz:    """).upper()

print(f"""
      Bilgisayar hamlesi = {bilgisayar_hamlesi}
      Kullanıcı Hamlesi = {kullanici_hamlesi}""")

while kullanici_puan <= 3 or bilgisayar_puan <= 3:

    bilgisayar_hamlesi = random.choice(secim)

    kullanici_hamlesi = input("""
                            TAŞ, KAĞIT, MAKAS;        hamlenizi giriniz:    """).upper()
    print(f"""
      Bilgisayar hamlesi = {bilgisayar_hamlesi}, {bilgisayar_puan}
      Kullanıcı Hamlesi = {kullanici_hamlesi}, {kullanici_puan}""")

    if kullanici_hamlesi in secim:
        #print("Oyuna devam") 

        if bilgisayar_hamlesi == kullanici_hamlesi :
            print("Berabere!!!")

        if bilgisayar_hamlesi == "MAKAS":
            if kullanici_hamlesi == "KAĞIT":
                print("Kullanıcı kesildi")
                bilgisayar_puan +=1
            if kullanici_hamlesi == "TAŞ":
                print("bilgisayar kırıldı")
                kullanici_puan +=1

        if bilgisayar_hamlesi== "TAŞ": 
            if kullanici_hamlesi == "KAĞIT":
                print("bilgisayar buruştu")
                kullanici_puan +=1
            if kullanici_hamlesi == "MAKAS":
                print("kullanıcı kırıldı")
                bilgisayar_puan +=1

        if bilgisayar_hamlesi== "KAĞIT": 
            if kullanici_hamlesi == "TAŞ":
                print("kullanıcı buruştu")
                bilgisayar_puan +=1
            if kullanici_hamlesi == "MAKAS":
                print("bilgisayar kesildi")
                kullanici_puan +=1

    else:
        print("doğru yaz şunu!!")


    if kullanici_puan == 3:
        print("Oyuncu WIN")
        break

    if bilgisayar_puan ==3:
        print("bilgisayar WIN")
        break