#RegNo 2367413  Name:Nishant    Prog:Scaler product
a = []
n = int(input("Enter number of elements in vector : "))
print("enter elements of vector A")
for i in range(0, n):
    l = float(input())
    a.append(l)
print("Vector a = ",a)
scaler = int(input("enter scaler qty"))
b= []
for i in range (0,n):
    b.append(a[i]*scaler)
print("new vector=",b)
