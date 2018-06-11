m,n=map(int,input("no. of dimension").lower().split('x'))
A=[]
for i in range(m):
    a=[]
    for j in range(n):
        a.append(int(input("enter at a")))
    A.append(a)
    print(A)
for i in range(m):
    for j in range(n):
        A[i][j]+=int(input("enter at b"))
print(A)
