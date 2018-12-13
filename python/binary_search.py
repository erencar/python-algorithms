## Binary Search (İkili Arama) Algoritması - Eren ÇAR

dizi=[1,2,45,78,95,105]
bas=0
sayac=0
son=len(dizi)-1
aranan=int(input("Aramak Istediginiz Degeri Girin \n"))

while bas <= son:
        orta=int((bas + son) / 2)

        if dizi[orta] == aranan:
            print("\n Aradiginiz sayi ",orta,". dizinde bulunmustur.")
            sayac=sayac+1
            break
        elif aranan > dizi[orta]:
            bas=orta+1

        else:
            son=orta-1

if sayac == 0:
    print("\n Aradiginiz sayi bulunamamistir")
