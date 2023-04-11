a,k,n=map(int,input().split())
result=[]
b=(k-(a%k))%k
   
while a+b<=n:
    if b!=0:
        result.append(b)
    b+=k
if len(result)==0:
     print("-1")

else: 
     for i in result:
        print(i,end=' ')
          