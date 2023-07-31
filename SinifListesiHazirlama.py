import datetime


class Student:
    def __init__(self, isim, soyisim, tc_no, dgtarihi):
        print("END101 öğrencisi")
        self.name = isim
        self.surname = soyisim
        self.tcno = tc_no
        self.__birthdate = dgtarihi


    def GetAge(self):
        bugun = datetime.date.today()
        age = bugun.year - self.__birthdate.year
        yas = str(age)
        return yas




class New:
    def KayitGir(self):
        self.END101=list()

        while True:
            isim = input("isim:")
            if (isim == "q"):
                break
            soyisim = input("soyisim:")
            tc_no = input("tc no:")
            yil = int(input("yıl:"))
            ay = int(input("ay:"))
            gun = int(input("gün:"))
            dgtarihi = datetime.date(yil, ay, gun)
            self.END101.append(Student(isim, soyisim, tc_no, dgtarihi))
        return

    def Listele(self):
        for i in self.END101:
            print(i.name, "", i.surname, "", i.tcno, "", i.GetAge())
        return

    def Remove(self):
        while True:
            silinecek = input("silinecek öğrencinin soyismi:")
            if silinecek=="end":
                break
            for i in self.END101:
                if (i.surname==silinecek):
                    del_name = input("silinmek istenen öğrencinin ismi:")
                    del_tc = input("silinmek istenen öğrencinin tc'si:")
                    if i.name==del_name:
                        if i.tcno==del_tc:
                            onay = input("onayınız(evet/hayır yazabilirsiniz.):")
                            if onay=="hayır":
                                break
                            elif onay=="evet":
                                print("**Remove Successed for ", i.name, i.surname)
                                self.END101.remove(i)
                                break
            else:
                print("--> Yanlış bilgi girdiniz! Listede var olan birini girin.<--")

        return


student1 = New()


def Cik():
    global b
    b = False


b = True
while (b):
    dic = {"1": New.KayitGir, "2": New.Listele, "3": New.Remove}
    print("1. Kayıt Girişi ")
    print("2. Sınıf Listesi")
    print("3.Silme ")
    print("x. Çık  ")

    sec = input("Seçiminiz ")
    if (sec == "x"):
        break

    dic[sec](student1)


