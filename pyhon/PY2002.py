a=[None]*100
a[0]=0
a[1]=1
a[2]=1
for i in range(3,93):
    a[i]=a[i-1]+a[i-2]
for i in range (int(input())):
    c,b=map(int,input().strip().split())
    for j in range(c,b+1,1):
        print(a[j],end=' ')
    print()
