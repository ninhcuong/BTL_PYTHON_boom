p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(1): 
     a=input()
     check=""
     if a=="0":
         break
     c=list(a.strip().split())
     k=int(c[0])
     s=c[1]
     for i in s:
           x=p.index(i)
           x=(x+k)%28
           check=p[x]+check
     print(check)
           
        

         