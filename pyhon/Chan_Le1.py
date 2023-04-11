def check(a):
   sum=0
   kt=True
   for i in range(len(a)-1):
         if int(a[i])-int(a[i+1])==2 or int(a[i])-int(a[i+1])==-2 :
               sum+=int(a[i])
         else :
             kt= False
             break
   sum=sum+int(a[len(a)-1])
   if(sum%10)!=0:kt=False
   return kt
for i in range(int(input())):  
      a=input()
      print("YES") if(check(a)) else print("NO")

   
      