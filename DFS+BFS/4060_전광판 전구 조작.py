def turnon(i,j):
    if i <= -1 or i >= m or j<=-1 or j>=n:
        return False
    if light[i][j]==0:
        light[i][j]=2
        turnon(i-1,j)
        turnon(i,j-1)
        turnon(i+1,j)
        turnon(i,j+1)
        return True
    return False

def turnoff(i,j):
    if i<=-1 or i>=m or j<=-1 or j>=n:
        return False
    if light[i][j]==1:
        light[i][j]=0
        turnoff(i-1,j)
        turnoff(i,j-1)
        turnoff(i+1,j)
        turnoff(i,j+1)
        return True
    return False

m,n=map(int,input().split())
light=[]
for i in range(m):
    light.append(list(map(int,input().split())))

ton=0
toff=0
for i in range(m):
    for j in range(n):
        if turnon(i,j)==True:
            ton+=1
for i in range(m):
    for j in range(n):
        if turnoff(i,j)==True:
            toff+=1
           
print(ton,toff)
