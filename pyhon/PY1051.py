def check(a): 
    kt=True
    
    dem=0
    for i in range (len(a)):
        dem+=int(a[i])
    s=str(dem)
    if(len(s)<2) : kt=False
    s1=s[::-1]
    if int(s)!= int(s1) : kt=False
    return kt
for i in range (int(input())):
    a=input()
    print("YES") if(check(a)) else print("NO")
