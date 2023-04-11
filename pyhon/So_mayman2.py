a=int(input())
for i in range(a):
    mayman=input()
    check1=mayman.count('4')
    check2=mayman.count('7')
    print("YES") if check1+check2==len(mayman) else print("NO")