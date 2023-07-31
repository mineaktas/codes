
class Ogrenci:
    def __init__(self, tc, isim, soyisim):
        self.tc=tc
        self.isim=isim
        self.soyisim=soyisim
        self.dtarih=""

    def GetName(self):
        return self.isim + " " + self.soyisim

    def GetFullInf(self):
        return self.tc + " " + self.GetName()

    def SetBirthDate(self, s):
        self.dtarih=s

    def Write(self):
        print(self.GetFullInf())


class Sinif:
    def __init__(self, sinif, kod):
        self.sinifAdi=sinif
        self.kod=kod
        self.ogrenciler=list()

    def AddStudent(self, ogr):
        self.ogrenciler.append(ogr)

    def GetClassInfo(self):
        return self.sinifAdi+ "  "+ self.kod

    def Write(self):
        print(self.GetClassInfo())
        print("------------------")
        for i in self.ogrenciler:
            i.Write()

    def Erase(self,s):
        for i in self.ogrenciler:
            if (i.soyisim == s.soyisim and i.isim == s.isim and i.tc == s.tc):
                self.ogrenciler.remove(i)
                break

    def FindStudent(self, s):
        for i in self.ogrenciler:
            if (i.soyisim == s.soyisim and i.isim == s.isim and i.tc == s.tc):
                return i
        return None

    def Remove(self, sn):
        liste=list()
        for i in self.ogrenciler:
            if (i.soyisim == sn):
                liste.append(i)

        if (len(liste)==0):
            print("Öğreci Bulunamadı")
            return

        if (len(liste)>1):
            ii=0
            for i in liste:
                ii +=1
                print(ii, " ", i.tc, "  ", i.isim, "  ", i.soyisim)
            sec=input("Silinecek kişiyi seç : ")
            ogrS = self.FindStudent(liste[int(sec)-1])
            self.Erase(ogrS)
        else:
            self.Erase(liste[0])



def CreateClass():
    s=input("Sınıf ismi : ")
    skod=input("Sınıf Kodu : ")
    snf=Sinif(s,skod)
    siniflar.append(snf)
    return snf

def AddStudent():
    ad=input("İsim : ")
    sad=input("Soyisim : ")
    tck=input("Tc Kimlik :")
    dt=input("Doğum Tarihi : ")
    sk=input("Sınıf Kodu : ")
    ogr=Ogrenci(tck, ad,sad)
    ogr.SetBirthDate(dt)
    for i in siniflar:
        if (i.kod == sk):
            i.AddStudent(ogr)

def Liste():
    sk= input("Sinif Kodu")
    for i in siniflar:
        if (i.kod == sk):
            i.Write()

def ListAll():
    for i in siniflar:
        i.Write()

def Remove():
    sn=input("Soyismi : ")
    snf=input("Sınıf Kodu : ")
    for i in siniflar:
        if (i.kod == snf):
            i.Remove(sn)


siniflar=[]

function={"0":CreateClass, "1":AddStudent, "2":Liste, "3":ListAll, "4":Remove}


while True:
    print("0 - Sınıf Oluştur")
    print("1 - Öğrenci ekle")
    print("2 - Sınıf Listesi")
    print("3 - Tüm Sınıfların Listesi")
    print("4 - Öğrenci sil ")
    print("x - Çık")
    secim =input ("Seçiminiz : ")
    if (secim=="x"):
        print("iyi günler")
        break
    if (int(secim)>=0 and int(secim)<=4):
        function[secim]()










'''
s0=Sinif("Endüstri-1", "End1")
ogr0=Ogrenci("43290", "Ali", "Dur")
ogr1=Ogrenci("43291", "Veli", "Dur")
ogr2=Ogrenci("43292", "Ahmet", "Git")

s0.AddStudent(ogr0)
s0.AddStudent(ogr1)
s0.AddStudent(ogr2)

s0.Write()
s0.Remove("Git")
s0.Remove("Dur")
s0.Write()
'''




