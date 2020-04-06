for _ in range(int(input())):
    s=list(input());stack=[]
    m=int(max(s))
    for i in range(10):
        stack=[]
        j=0;end=len(s)
        while(True):
            if(j==end):
                break
            #print(s,stack,s[j],i)
            if(s[j]==')' or s[j]=='('):
                pass
            elif(int(s[j])>i and len(stack)==0):
                stack.append(')')
                s=s[:j]+['(']+s[j:]
                end+=1

            elif(int(s[j])<=i and len(stack)>0):
                stack.pop(-1)
                s=s[:j]+[')']+s[j:]
                end+=1
    
            j+=1
        s.extend(stack)
        #print(s,stack)
        if(i==m):
            break
    #print("".join(s))
    print("Case #",_+1,": ","".join(s),sep="")
