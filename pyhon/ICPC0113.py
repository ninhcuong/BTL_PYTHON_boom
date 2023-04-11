import math
global a 
def  snt():
    a[0]=False
    a[1]=False
    for i in range (2,10**6,1):
     if a[i]==True :
        for j in range(i*i,10**6,i):
            a[j]=False
def check(i,n):
    b=str(i)
    b=b[::-1]
    if int(b)!=i and a[int(b)]==True and a[i]==True and int(b)<n:
        print(i,int(b),end=" ")
        a[int(b)]=False
        a[i]=False
a=[True]*10**6
for i in range(int(input())):
    snt()
    n=int(input())
    for i in range(n):
        check(i,n)
    a=[True]*10*10**6
    print()