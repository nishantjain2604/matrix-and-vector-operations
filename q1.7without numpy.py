#RegNo 2367413  Name:Nishant    Prog:Inverse of matrix
a=[[ 2,  3,  1,  1, 0, 0],
    [ 3, 3,  1, 0, 1, 0],
    [ 2,  4,  1, 0, 0, 1]]
n=len(a)
def print_matrix(m1,R,C):
    for i in range(R):
        for j in range(C):
            print(m1[i][j], end=" ")
        print()
for i in range (n):
    pivot = 1/a[i][i]
    for j in range (n+n):
        a[i][j]=pivot*a[i][j]
    for k in range(n):
        if i != k:
            pivot = a[k][i]
            for j in range (n+n):
                    a[k][j]=a[k][j]-pivot*a[i][j]
x=[]
for i in range (n):
    b=[]
    for j in range (n,n+n):
        b.append(a[i][j])
    x.append(b)
print_matrix(x,n,n)


