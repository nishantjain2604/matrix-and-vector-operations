#RegNo 2367413  Name:Nishant    Prog: Rank of Matrix
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
def rank(a,R,C):
    f = min(R, C)
    count = 0
    x=0
    for i in range(f):
        if a[i][i] == 0:
            x+=1
        else:
            count += 1
    return count
for i in range (min(Row, Column)):
        if a[i][i]==0:
            for j in range(i + 1, Row):
                if a[j][i] != 0:
                    a[i][j] = a[j][i]
                    break
        else:
            pivot = 1/a[i][i]
            for j in range (Column):
                a[i][j]=pivot*a[i][j]
            for k in range(Row):
                if i != k:
                    pivot = a[k][i]
                    for j in range (Column):
                            a[k][j]=a[k][j]-pivot*a[i][j]
r= rank(a, Row, Column)
print("rank=",r)
