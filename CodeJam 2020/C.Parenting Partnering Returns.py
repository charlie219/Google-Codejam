for _ in range(int(input())):
    n=int(input())
    boo=True
    c=[];jx=[];ans=""
    ta=[]
    for i in range(n):
        t=list(map(int,input().split()))
        ta.append(sorted(t))
    task=sorted(ta);dic={}
    #print(task)
    for i in task:
        dic[(i[0],i[1])]=[]
    for i in range(n):
        allot=False
        a,b=task[i][0],task[i][1]
        if(len(c)==0):
            dic[(a,b)].append('C')
            c.append([a,b])
            allot=True
        if(not allot):
            xyz=True
            for j in c:
                if(j[0]<=a<j[1]):
                    xyz=False
                    break
            if(xyz):
                dic[(a,b)].append('C')
                c.append([a,b])
                allot=True
        if(not allot and len(jx)==0):
            dic[(a,b)].append('J')
            jx.append([a,b])
            allot=True
        if(not allot):
            xyz=True
            for j in jx:
                if(j[0]<=a<j[1]):
                    xyz=False
                    break
            if(xyz):
                dic[(a,b)].append('J')
                jx.append([a,b])
                allot=True
        if(not allot):
            boo=False
            break
    #print(dic)
    if(not boo):
        ans='IMPOSSIBLE'
    else:
        for i in ta:
            ans+=dic[(i[0],i[1])][0]
            if(len(dic[(i[0],i[1])])>1):
                dic[(i[0],i[1])].pop(0)
                
    #print(c,jx)
    print("Case #",_+1,": ",ans,sep="")
