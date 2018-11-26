#eliminacion gaussiana
#4x1 + x2 -x3=0 
#2x1 +5x2 + 2x3=3
#x1 + 2x2 + 4x3 =11
def creatematriz (m,n,v):
    c=[]
    for i in range(m):
        c.append([])
        for j in range(n):
            c[i].append(v)
    return c
MA = creatematriz(3,4,0)
MA[0]=[4,1,-1,0]
MA[1]=[2,5,2,3]
MA[2]=[1,2,4,11]

MAm=3
MAn=4
for i in range (MAm):
    pivote =MA[i][i]
    if pivote==0: #intercambio renglones
        for j in range(i+1,MAm):
            pivote=MA[j][i]
            if pivote !=0:
                T=MA[i]
                MA[i]=MA[j]
                MA[j]=T
                break
    for k in range(MAn):
        MA[i][k]=(1/pivote)*MA[i][k]
    for j in range(i+1,MAm):
        c=-1*MA[j][i]
        T= creatematriz(1,MAn,0)
        for k in range(MAn):
            T[0][k]=c*MA[i][k]
        for k in range(MAn):
            MA[j][k]+=T[0][k]
print("EG",MA)
B=creatematriz(3,1,0)
for i in range(MAm-1,-1,-1):
    B[i][0]=MA[i][MAn-1]
    for j in range(MAn-2,-1,-1):
        if i==j:
            break
        B[i][0]-=MA[i][j]*B[j][0]
print(B)

