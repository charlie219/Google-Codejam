def cal(s):
    count=s.count("*")
    ans=[s,0]
    if(count>=2):
        l=s.index('*');r=0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='*'):
                r=i
                break
        x=''
        for i in range(l,r):
            if(s[i]!='*'):
                x+=s[i]
        ans=[s[:l]+x+s[r+1:],1]
    return ans
    
for _ in range(int(input())):
    n=int(input());s=[];boo=True
    l='';r='';do=[];left=[];right=[];lm=['',''];rm=['','']
    s=[]
    for i in range(n):
        a=input()
        s.append(a)
        if(a[0]!='*'):
            if(l==''):  l=a[0]
            else:
                if(a[0]!=l):
                    boo=False
            x=a[:a.index("*")]
            lm=[x,a] if len(x)>len(lm[0]) else lm
            left.append([a,x])
        if(a[-1]!='*'):
            if(r==''):  r=a[-1]
            else:
                if(a[-1]!=r):
                    boo=False
            x=''
            for j in range(len(a)-1,-1,-1):
                if(a[j]=='*'):
                    count=j
                    break
                x+=a[j]
            x=x[::-1]
            rm=[x,a] if len(x)>len(rm[0]) else rm
            right.append([a,x])
    #print(lm[0],rm[0])
    for i in left:
        if(i[1] not in lm[0]):
            boo=False
            break
    for i in right:
        if(i[1] not in rm[0]):
            boo=False
            break
    if(not boo):
        #print("*")
        print("Case #",_+1,": *",sep="")
        continue
    ans=lm[0] if len(lm)>0 else ''
    for i in s:
        c=cal(i)
        if(c[1]==1):
            do.append(c[0])
    
        
    for i in do:
        ans+=i
    ans+=rm[0] if len(rm)>0 else ''
    #print(ans)
    print("Case #",_+1,": ",ans,sep="")
