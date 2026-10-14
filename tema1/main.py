import math

def det(A):
    deter = 0
    if len(A) == 0:
        return 1
    for i in range(len(A)):
        if len(A[i]) != len(A):
            return -1

    if len(A)==1:
        return A[0][0]
    for i in range(len(A)):
        A1=[]
        for j in range(1,len(A)):
            l=[]
            for k in range(len(A)):
                if k!=i:
                    l.append(A[j][k])
            A1.append(l)
        if i%2==0:
            deter+=A[0][i]*det(A1)
        else:
            deter-=A[0][i]*det(A1)


    return deter
def trace(A):
    tr=0
    for i in range(len(A)):
        tr+=A[i][i]
    return tr

def norm(A):
    norm=0

    for i in range(len(A)):
        norm+=A[i]**2
    return math.sqrt(norm)

def trans(A):
    T=[]
    for i in range(len(A[0])):
        lin=[]
        for j in range(len(A)):
            lin.append(A[j][i])
        T.append(lin)

    return T

def mul(A,B):
    M=[]
    for i in range(len(A)):
        s=0
        for j in range(len(B)):
            s+=A[i][j]*B[j]
        M.append(s)
    return M
def cramer(A,B):
 if det(A)!=0:
    S=[]
    for i in range(len(A)):
        CR=[]
        for j in range(len(A)):
            l=[]
            for k in range(len(A)):
                if k==i:
                    l.append(B[j])
                else :
                    l.append(A[j][k])

            CR.append(l)
        S.append(det(CR)/det(A))
    return S
 else :
     return -1

def Inv(A,B):
  if det(A)!=0:
    Co=[]
    for i in range(len(A)):
       l=[]
       for j in range(len(A)):
           M=[]
           for k in range(len(A)):
               if k!=i:
                   M.append(A[k][:j]+A[k][j+1:])

           l.append((-1) ** (i+j) * det(M))
       Co.append(l)
    Ad=trans(Co)
    for i in range(len(A)):
        for j in range(len(A)):
            Ad[i][j]=Ad[i][j]/det(A)
    return mul(Ad,B)
  else :
    return -1

def Parse(fis):
 fis=open(fis,"r")
 A=[]
 B=[]
 C=[]
 for i in fis:
    lin=i.split("=")
    a=lin[0].split()
    val={}
    l=[]
    semn=1
    for j in a:
        if j=="+":
            semn=1
        elif j=="-":
            semn=-1
        else:
            if j !="":
                if j[-1].isalpha():
                    var=j[-1]
                    num=j[:-1]

                    if num == "":
                        num=1
                    else :
                        num=int(num)
                    if var not in C:
                        C.append(var)
                    val[var]=semn*num
                    semn=1
    for var in C:
        if var in val:
            l.append(val[var])
        else:
            l.append(0)
    A.append(l)
    B.append(int(lin[1].strip()))

 fis.close()
 return A,B,C

A, B, C = Parse("exe.txt")
print("A = ",A)
print("B = ", B)
print("C = ",C)

print("DET = " ,det(A))

print("TR = " , trace(A))

print("NORM =" , norm(B))

print("TRANSP = ",trans(A))

print("MUL = ", mul(A,B))

S=cramer(A,B)
print("SOL CRAMER = " ,S)

S2=Inv(A,B)
print("SOL INV = " ,S2)