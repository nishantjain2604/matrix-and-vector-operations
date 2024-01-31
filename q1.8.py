#RegNo 2367413  Name:Nishant    Prog:Simultaneous Linear equation
a=[[ 1,  2,  3,  14],
    [ 3, 2,  1, 10],
     [3, 1, 2, 11,]]
n=len(a)
for i in range (n):
    pivot = 1/a[i][i]
    for j in range (n+1):
        a[i][j]=pivot*a[i][j]
    for k in range(n):
        if i != k:
            pivot = a[k][i]
            for j in range (n+1):
                    a[k][j]=a[k][j]-pivot*a[i][j]
for i in range (n):
    print("x",i,"=",a[i][n])
