for _ in range(int(input())):
    n=int(input())
    a=[[int (i) for i in input().split()] for j in range(n)]
    k=0;r1=0;c1=0
    for i in range(n):
        r=a[i]
        c=[a[j][i] for j in range(n)]
        #print(r,c)
        if(len(set(r))!=n):
            r1+=1
        if(len(set(c))!=n):
            c1+=1
        k+=a[i][i]
    print("Case #",_+1,": ",k," ",r1," ",c1,sep="")
