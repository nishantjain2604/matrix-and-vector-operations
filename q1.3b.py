#RegNo 2367413  Name:Nishant    Prog:Inner product
a = []
n = int(input("Enter number of elements in vector : "))
print("enter elements of vector A")
for i in range(0, n):
    l = float(input())
    a.append(l)
print("Vector a = ",a)
b = []
print("enter elements of vector B")
for i in range(0, n):
    m = float(input())
    b.append(m)
print("Vector b = ",b)
c= 0
for i in range (0,n):
    c= c+ (a[i]*b[i])
print("Inner product =", c)
