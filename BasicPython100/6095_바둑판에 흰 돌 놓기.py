arr=[]
change=[]
for i in range(19):
    b=input().split()
    arr.append(b)
    
n=int(input())
for i in range(n):
    x,y=input().split()
    for j in range(19):
        arr[int(x)-1][j]=(int(arr[int(x)-1][j])+1)%2
        arr[j][int(y)-1]=(int(arr[j][int(y)-1])+1)%2

for i in range(19):
    for j in range(19):
        print(arr[i][j],end=' ')
    print()
