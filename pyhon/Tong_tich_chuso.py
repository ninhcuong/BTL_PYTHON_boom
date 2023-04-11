for i in range (int(input())):
     a=input()
     check=True
     c=0
     l=1
     for i in range (len(a)):
        if(i%2!=0): 
            c+=int(a[i])
        elif int(a[i])!=0:
            l*=int(a[i])
            check=False
     if(check==True) :l=0
     print(l,c)
     
