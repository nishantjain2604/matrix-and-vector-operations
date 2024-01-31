print("RegNo 2367413  Name:Nishant    Prog: Matrix addition")
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
matrixA = read(Row,Column)
print("matrix A = ")
print_matrix(matrixA,Row,Column)
matrixB = read(Row,Column)
print("matrix B = ")
print_matrix(matrixB,Row,Column)
sum=[]
for i in range (Row):
    c=[]
    for j in range (Column):
        c.append(matrixA[i][j]+matrixB[i][j])
    sum.append(c)
print("sum of the 2 matrix is")
print_matrix(sum,Row,Column)
