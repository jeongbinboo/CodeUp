def search(i,j):
    if i<=-1 or i>=m+1 or j<=-1 or j>=n+1:
        return False
    if area[i][j]==0:
        area[i][j]=1
        search(i-1,j)
        search(i,j-1)
        search(i,j+1)
        search(i+1,j)
        return True
    return False

m,n,k=map(int,input().split())
square=[]
area=[]
cnt=0

for i in range(m+1):
    line=[]
    for j in range(n+1):
        line.append(0)
    area.append(line)

for i in range(k):
    square.append(list(map(int,input().split())))
    x1=m-square[i][1]
    y1=square[i][0]
    x2=m-square[i][3]
    y2=square[i][2]
    x3=min(x1,x2)
    y3=min(y1,y2)
    x4=max(x1,x2)
    y4=max(y1,y2)
    for j in range(x3,x4+1):
        for k in range(y3,y4+1):
            area[j][k]=1

for i in range(m+1):
    for j in range(n+1):
        if search(i,j)==True:
            cnt+=1
print(cnt)
