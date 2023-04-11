import math
for i in range(int(input())): 
   n=int(input())
   k="1"
   dem=0
   for i in range(2,int(math.sqrt(n)),1): 
        while(n%i==0):  
             dem+=1
             n=n/i
        if(dem>0): 
            k=k+" * "+str(i)+"^"+str(dem)
            dem=0
   if(n>1) :k=k+" * "+str(int(n))+"^"+"1"
   print(k)
