a=input()
check=0
for i in range (len(a)):
    if a[i]=='4' or a[i]=='7':
        b=int(a[i])
        check+=1
if check==4 or check==7:
    print("YES")
else:
    print("NO")