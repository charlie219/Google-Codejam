global mat
def compass(mat):
    r=len(mat);c=len(mat[0])
    avgmat=[[0]*c for i in range(r)]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            temp=0;count=0
            for a in range(i-1,-1,-1):
                if(mat[a][j]!=0):
                    temp+=mat[a][j];count+=1
                    break
            for a in range(i+1,r):
                if(mat[a][j]!=0):
                    temp+=mat[a][j];count+=1
                    break
            for b in range(j-1,-1,-1):
                if(mat[i][b]!=0):
                    temp+=mat[i][b];count+=1
                    break
            for b in range(j+1,c):
                if(mat[i][b]!=0):
                    temp+=mat[i][b];count+=1
                    break
            if(count==0):   avgmat[i][j]=mat[i][j]
            else:   avgmat[i][j]=temp/count
            #print(i,j,avgmat[i][j])
    #print(avgmat)
    return avgmat

def elimination(mat):
    avg=compass(mat);boo=False
    #print("**",avg)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if(mat[i][j]<avg[i][j] and mat[i][j]!=0):
                boo=True
                mat[i][j]=0

    return boo
                
for _ in range(int(input())):
    r,c=map(int,input().split())
    mat=[[int(i) for i in input().split()] for j in range(r)]
    s=sum([sum(mat[i]) for i in range(len(mat))])
    while(elimination(mat)):
        s+=sum([sum(mat[i]) for i in range(len(mat))])
        #print(mat)
    #s+=sum([sum(mat[i]) for i in range(len(mat))])
    #print(s)
    print("Case #",_+1,": ",s,sep="")
