def pang(x,y,cmp):
    global cnt
    if x<0 or x>=7 or y<0 or y>=7:
        return 0
    if candy[x][y]==cmp:
        candy[x][y]=0
        cnt+=1
        pang(x-1,y,cmp)
        pang(x+1,y,cmp)
        pang(x,y-1,cmp)
        pang(x,y+1,cmp)
        return cnt
    return 0

candy=[]
cnt=0
res=0
for i in range(7):
    candy.append(list(map(int,input().split())))

for i in range(7):
    for j in range(7):
        cnt=0
        if candy[i][j]!=0:
            if pang(i,j,candy[i][j])>=3:
                res+=1
print(res)
