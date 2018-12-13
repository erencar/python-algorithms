## Bubble Sort (Kabarcık Sıralama) Algoritması - Eren ÇAR

dizi=[4,8,1,2,5]
n= len(dizi)

for i in range(n):

     for j in range(0, n- i - 1):

        if dizi[j] > dizi[j + 1]:
            dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]

for i in range(n):
    print(dizi[i])
