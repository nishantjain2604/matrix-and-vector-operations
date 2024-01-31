print("RegNo 2367413  Name:Nishant    Prog: Rank of Matrix")
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
def read(R,C):
    m1=[]
    print("Enter the entries row wise:")
    for i in range(R):
        a = []
        for j in range(C):
            a.append(int(input()))
        m1.append(a)
    return m1
def print_matrix(m1,R,C):
    for i in range(R):
        for j in range(C):
            print(m1[i][j], end=" ")
        print()
a = read(Row,Column)
print("matrix A = ")
print_matrix(a,Row,Column)
f=min(Row,Column)
def rank(a,R,C,f):
    count = 0
    x=0
    for i in range(f):
        if a[i][i] == 0:
            x+=1
        else:
            count += 1
    temp=[x,count]
    return temp
g= [0,0]
for i in range (Row):
        if a[i][i]==0:
            g[0]+=1
        else:
            pivot = 1/a[i][i]
            for j in range (Column):
                a[i][j]=pivot*a[i][j]
            for k in range(Row):
                if i != k:
                    pivot = a[k][i]
                    for j in range (Column):
                            a[k][j]=a[k][j]-pivot*a[i][j]
r= rank(a, Row, Column, f)
print("rank=",r[1])
