n,m = map(int,input("Enter matrix dimension m n : ").lower().split())
#A = [ [ int(input("A[{}][{}] = ".format(row,col))) for col in range(m) ] for row in range(n) ]
def show(X):
    for var in X:
        s = '{:10}'*len(var)
        print('\t',s.format(*var))

print("Please Give matrix A : ")
A = [ list(map(int,input('\t').split())) for var in range(n) ]
print("Please Give matrix B : ")
B = [ list(map(int,input('\t').split())) for var in range(n) ]
print("Matrix A is : ")
show(A)
print("Matrix B is : ")
show(B)
c=int(input("enter 1-multi 2-add 3-transpose"))
if c==3:
    result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    for r in result:
        print (r)
    result = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
    for s in result:
        print (s)
elif c==2:
    add = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    for a in add:
        print (a)
elif c==1:
    zero = [0 for j in range(0,0) for i in range(0,0)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                zero[i][j] +=A[i][k]*B[k][j]
    for m in zero:
        print(m)
