for i in range (int(input())):
    c,b=map(int,input().split())
    a=list()
    while len(a)<c:
      a=[int(i) for i in input().split()]
    for i in range(b,len(a),1):
        print(a[i],end=' ')
    for j in range(b):
        print(a[j],end=' ')
    print()
