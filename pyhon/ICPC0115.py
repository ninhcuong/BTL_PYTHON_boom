t=int(input())
a=list(map(int,input().split()))
em=0
for i in range (len(a)-1):
    if(a[i]!=a[i+1]):
        em+=1
print(em)
    