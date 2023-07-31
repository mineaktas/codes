import xlrd
import xlwt

locx="c://temp//excelfonk.xlsx"
p=0
wb=xlrd.open_workbook(locx)
sheet=wb.sheet_by_index(p)
r=sheet.nrows
c=sheet.ncols

class MTRS:
    def __init__(self,r,c):
        self.r=sheet.nrows
        self.c=sheet.ncols
        self.mtx=[]
        self.satir=[]


    def SetMtrs(self):
        for i in range(r):
            self.satir=[]
            for j in range(c-3):
                v = sheet.cell_value(i, j)
                self.satir.append(v)
            self.mtx.append(self.satir)
        return self.mtx

    def Set2Matris(self):
        for i in range(r):
            self.satir = []
            for j in range(c-2,c ):
                v = sheet.cell_value(i,j)
                self.satir.append(v)
            self.mtx.append(self.satir)
        return self.mtx

k=MTRS(r,c)
l=MTRS(r,c)
A=k.SetMtrs()
B=l.Set2Matris()
print(A)
print(B)
f=sheet.cell(0,2).value
print(f)


class Result():
    def __init__(self,toplam,fark,carpim,bolum):
        self.toplam=toplam
        self.fark=fark
        self.carpim=carpim
        self.bolum=bolum
        self.list=[]

    def Fonksiyon(self):
        if f=="Topla":
            for i in range(len(A)):
                for j in range(len(A[0])):
                    self.toplam=A[i][j]+B[i][j]
                    self.list.append(self.toplam)
            print(self.list)

        elif f=="Çıkarma":
            for i in range(len(A)):
                for j in range(len(A[0])):
                    self.fark=A[i][j]-B[i][j]
                    self.list.append(self.fark)
            print(self.list)

        elif f=="Çarpma":
            for i in range(len(A)):
                for j in range(len(A[0])):
                    self.carpim=A[i][j]*B[i][j]
                    self.list.append(self.carpim)
            print(self.list)

        elif f=="Bölme":
            for i in range(len(A)):
                for j in range(len(A[0])):
                    self.bolum=A[i][j]/B[i][j]
                    self.list.append(self.bolum)
            print(self.list)

        else:
            print("4 işlemden birini seçiniz!")

        return self.list

e=Result(toplam=(),fark=(),carpim=(),bolum=())
C=e.Fonksiyon()

wbiki = xlwt.Workbook()

ws = wbiki.add_sheet("test")

ws.write(8,8,str(C))

wbiki.save('sonucdosyası.xls')
