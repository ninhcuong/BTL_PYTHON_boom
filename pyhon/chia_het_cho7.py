for i in range (int(input())): 
    check=True
    a=input()
    n=a
    sum=0
    for i in range(1,1001,1): 
        if(int(n)%7)==0: 
             check=False
             break
        else :
             sum=int(n)+int(n[::-1])
             n=str(sum)
             if(sum%7==0): 
                check=False
                break
    if(sum%7)==0: 
        print(n)
    elif check==True:
        print("-1")
             