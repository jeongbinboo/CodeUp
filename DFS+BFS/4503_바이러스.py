n=int(input())
m=int(input())
cp=[]
chk=[]
for i in range(n):
    cp.append([0,0,0,0,0,0,0])
    chk.append(0)
for i in range(m):
    a,b=map(int,input().split())
    cp[a-1][b-1]=1
    cp[b-1][a-1]=1

print(cp)
print(chk)
