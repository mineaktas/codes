# Satır ve sütun sayısını giriyoruz. İki matrisin toplanabilmesi için her iki matrisin satır sayılarının ve sütun
# sayılarının birbirine eşit olması gerekir. mesela 2x3 bir matris ile 3x3 veya 3x2 bir matris toplanamaz.

M=int(input("Satır Sayısını giriniz: "))
N=int(input("Sütun Sayısını giriniz: "))

# M satır ve N sütun olarak girildi.
# Aşağıdaki bölümde A matrisinin her bir elemanı tek tek giriliyor.

print("A matrisini giriniz ")
matrisA=[]
matrisAsatir=[]

for i in range(0,M):
    matrisAsatir=[]
    for j in range(0,N):
        s=float(input("a("+str(i+1)+","+str(j+1)+")"))
        matrisAsatir.append(s) # i. satır oluşturuluyor. i. satır j. elemanı girişi yapılıyor.
    matrisA.append(matrisAsatir) #i. satır eklendi

# Aşağıdaki bölümde B matrisinin her bir elemanı tek tek giriliyor.

print("B matrisini giriniz ")
matrisB=[]
matrisBsatir=[]

for i in range(0,M):
    matrisBsatir=[]
    for j in range(0,N):
        s=float(input("b("+str(i+1)+","+str(j+1)+")"))
        matrisBsatir.append(s)
    matrisB.append(matrisBsatir)

# A matrisi ekrana yazdırıldı
print("Matris A ")
for i in matrisA:
    print(i)

# A matrisi ekrana yazdırıldı

print("Matris B ")
for i in matrisB:
    print(i)

#Burada matrisler toplanıyor.
toplam=[]
toplamS=[]
for i in range(0,M):
    toplamS = []
    for j in range(0,N):
        toplamS.append(matrisA[i][j]+matrisB[i][j]) # i. satırın j. elemanları karşılıklı olarak toplanıp toplam matrisin i. satırı hazırlanıyor
    toplam.append(toplamS) # toplam matrisin i. satırı ekleniyor

# toplam matrisi yazdırılıyor.
print("Toplam Matris ")
for i in toplam:
    print(i)
