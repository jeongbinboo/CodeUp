n,m=input().split()
n=int(n)
m=int(m)
status=[]
for i in range(n):
    room=input()
    status.append(room)
s,t=input().split()
s=int(s)
t=int(t)

move=0
y=0

for i in range(s-1,t-1):
    f=0
    if i != s-1:
        if status[i][y]=='O':
            continue
    for j in range(0,m):
        if status[i][j]=='O':
            if status[i+1][j]=='O':
                f=1
                y=j
                break
            else:
                y=j
                f2=1
                continue
    if f==0:
        print('-1')
        break
    
    if f2==1:
        move+=1
if f!=0:
    print(move)
