F=lambda c:c*(c+1)//2
def cal(n):
    x=int((2*n)**(1/2))
    if(F(x)<=n):
        return x
    else:
        return x-1
for _ in range(int(input())):
    n=int(input())-1;a=[[1,1]]
    x=cal(n)
    for i in range(2,x+2):
        a.append([i,2])
    for i in range(x+1,x+1+n-F(x)):
        a.append([i,1])
    #print(len(a),x)
    print("Case #",_+1,": ",sep="")
    for i in a:
        print(*i)
    #print(len(a))
