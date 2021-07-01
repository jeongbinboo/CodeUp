arr=[]
for i in range(10):
    arr.append(input().split())

x=1
y=1
while x!=9 and y!=9:
    if arr[x][y]=='2':
        arr[x][y]='9'
        break
    arr[x][y]=9
    if arr[x][y+1]=='0' or arr[x][y+1]=='2':
        y+=1
    elif arr[x+1][y]=='0' or arr[x+1][y]=='2':
        x+=1
    else:
        break
for i in range(10):
    for j in range(10):
        print(arr[i][j],end=' ')
    print()
