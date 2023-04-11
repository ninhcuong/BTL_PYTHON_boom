for i in range (int(input())):
    s=input()
    check=False
    dem=1
    for j in range(0,len(s)-1,1) :  
        if s[j]==s[j+1]:  
           dem+=1
           check=True
        else:
            print(dem,s[j],sep='',end='')
            dem=1
    print(dem,s[len(s)-1],sep='',end='')
    print()

            
