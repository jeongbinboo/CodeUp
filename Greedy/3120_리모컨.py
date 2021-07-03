c,g=input().split()
c=int(c)
g=int(g)
cnt=0

while c!=g:
    dif=g-c
    if dif>=8:
        c+=10
    elif dif>=4:
        c+=5
    elif dif>=1:
        c+=1
    elif dif<=-8:
        c-=10
    elif dif<=-4:
        c-=5
    else:
        c-=1
    cnt+=1
print(cnt)
