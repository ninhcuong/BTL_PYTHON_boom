def check(a):
    kt=True
    n=list("")
    for i in a:
         if i not in n: 
            n.append(i)
    
    if(len(n)<3) : kt=False
    check=0
    for i in range (len(a)-1): 
        if(a[i]==a[i+1]):
             kt=False
        if(a[i]>a[i+1]) :
            check=i
            break
    for i in range (check,len(a)-1,1):
         if(a[i]<a[i+1]): 
             kt=False
    return kt       
for i in range(int(input())):
     a=input()
     print("YES") if check(a) else print("NO")

