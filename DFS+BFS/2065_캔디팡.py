def pang(i,j,c):
    print(i,j)
    if i<0 or i>=7 or j<0 or j>=7:
        return 0
    if candy[i][j]==c:
        candy[i][j]=0
    return 1+pang(i-1,j,c)+pang(i+1,j,c)+pang(i,j-1,c)+pang(i,j+1,c)
candy=[]
res=0
for i in range(7):
    candy.append(list(map(int,input().split())))

for i in range(7):
    for j in range(7):
        cnt=0
        if pang(i,j,candy[i][j])>=3:
            res+=1
        
print(res)
print(candy)
