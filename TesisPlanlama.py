import MatrisYaz
def MatrisMinEleman(N, T, K):
    enk=N[0][0]
    for i in range(0,len(N)):
        for j in range(0,len(N[0])):
            if (enk>=N[i][j] and T[j]>0 and K[i]>0):
                enki=i
                enkj= j
                enk=N[i][j]
    return enki, enkj

def Atama(i, j, T, K, Atama):
    t=T[j]
    k=K[i]
    if (t<k):
        K[i]=k-t
        T[j]=0
        Atama[i][j]=t
    else:
        T[j]=t-k
        K[i]=0
        Atama[i][j] = k

def VektorSifirToplamli(V):
    t=0
    for i in V:
        t+=i
    return t>0

def AtamaMatrisi(N):
    m=[]
    for i in range(0,len(N)):
        satir=[]
        for j in range(0,len(N[0])):
            satir.append(0)
        m.append(satir)
    return m

Cost=[[80,	78,	77,	78,	77],
      [76.50,	75,	73.50,	71.50,	70.20],
      [71.50,	70.50,	71.80,	76.50,	75]]
Talep=[5000,6000,4000,7000,3000]
Kapasite=[7000,5500,12500]


AtamaMatrisi=AtamaMatrisi(Cost)

s=VektorSifirToplamli(Talep) or VektorSifirToplamli(Kapasite)
print(s)
while (s):
    i,j=MatrisMinEleman(Cost,Talep,Kapasite)
    Atama(i,j, Talep,Kapasite,AtamaMatrisi)
    MatrisYaz.WriteMatrix(AtamaMatrisi)
    print("-----------------")
    print("Talep :", Talep)
    s = VektorSifirToplamli(Talep) or VektorSifirToplamli(Kapasite)



