def find(cp):
    checked.append(cp)
    for i in range(n+1):
        if com[cp][i]==1 and i not in checked:
            find(i)

n=int(input())
m=int(input())
checked=[]

com=[[0]*(n+1) for i in range(n+1)]

for i in range(m):
    c1,c2=map(int,input().split())
    com[c1][c2]=com[c2][c1]=1
    

find(1)
print(len(checked)-1)
