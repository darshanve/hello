n,m = map(int,input("enter dimension m , n: ").lower().split())
def show(x):
    for  var in x:
        s='{:10}'*len(var)
        print('\t',s.format(*var))
print("matrix A:")
A=[list(map(int,input('\t').split())) for var in range(n)]
print("matrix B:")
B=[list(map(int,input('\t').split())) for var in range(n)]
print('A')
show(A)
print('B')
show(B)
