def check(a): 
      s=a[::-1]
      kt=True
      if int(s)!=int(a) : kt=False
      if(len(a)%2!=0) : kt=False
      for i in range(len(a)): 
        if(int(a[i])%2!=0) : 
             kt=False
             break
       
      return kt

for i in range(int(input())) :
     n=int(input())
     for i in range(20,n,2):
        if(check(str(i))) :
            print(i,end=' ') 
     print()
     
